#!/usr/bin/env python3
"""Supplemental finite numerical checks of a sine-map phase classification."""

import math
import random

PI = math.pi
CHECKS = 0


def near(a, b, tolerance=1e-10):
    global CHECKS
    assert abs(a - b) <= tolerance, (a, b, tolerance)
    CHECKS += 1


def circular_distance(a):
    return abs((a + PI) % (2 * PI) - PI)


def data(rho):
    return math.sqrt(1 - rho**-2), math.asin(1 / rho), math.sqrt(rho*rho - 1) - PI / 2


def number_of_sinks(rho, theta):
    _, h, c = data(rho)
    return int(circular_distance(theta-c) < h) + int(circular_distance(theta+c) < h)


def bisect(f, a, b):
    fa = f(a)
    fb = f(b)
    assert fa * fb <= 0
    for _ in range(72):
        mid = (a + b)/2
        fm = f(mid)
        if fa*fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return (a+b)/2


def brute_count(rho, theta):
    # A fine independent sign-change scan, used only away from boundaries.
    n = max(1800, int(120 * rho))
    def g(u):
        return math.sin(rho*u-theta)-u
    total = 0
    a, fa = -1.0, g(-1.0)
    for i in range(1,n+1):
        b = -1+2*i/n
        fb = g(b)
        if fa*fb < 0:
            root = bisect(g,a,b)
            if abs(rho*math.cos(rho*root-theta))<1-1e-7:
                total += 1
        a,fa = b,fb
    return total


def construct_sink(rho, theta, sign):
    # Solve monotone phase branches rather than iterating the map.
    if sign == -1:
        return -construct_sink(rho,-theta,+1)
    s,h,c = data(rho)
    lift = c + ((theta-c+PI)%(2*PI)-PI)
    assert abs(lift-c)<h
    cross = rho-PI/2
    if lift >= cross:
        f=lambda u: rho*u-math.asin(u)-lift
    else:
        f=lambda u: rho*u-PI+math.asin(u)-lift
    return bisect(f,s,1.)


for j in range(30):
    rho=math.hypot(1,(j+0.5)*PI)
    s,h,c=data(rho)
    near(c,j*PI,5e-13)
    near(number_of_sinks(rho,j*PI),2)
    for sign in (-1,1):
        root=construct_sink(rho,j*PI,sign)
        near(math.sin(rho*root-j*PI),root,5e-11)
        assert abs(rho*math.cos(rho*root-j*PI)) < 1
        CHECKS+=1

rng=random.Random(20231015)
for _ in range(220):
    rho=1.02+35*rng.random()
    theta=(2*rng.random()-1)*11*PI
    _,h,c=data(rho)
    margin=min(abs(circular_distance(theta-c)-h),abs(circular_distance(theta+c)-h))
    if margin<0.05:
        continue  # Sign scans are not certificates near a tangency.
    near(brute_count(rho,theta),number_of_sinks(rho,theta))

print('PASS:', CHECKS, 'finite assertions')
