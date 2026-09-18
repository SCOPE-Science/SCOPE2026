import heapq
import math


def b2(x):
    return x*x - x + 1.0/6.0


def b3(x):
    return x*x*x - 1.5*x*x + 0.5*x


def check(max_n=300000):
    p = [math.sqrt(2.0)/4.0, math.pi/12.0, 1.0-math.sqrt(2.0)/4.0-math.pi/12.0]
    d = len(p)
    m = [0]*d
    heap = [(-p[i], i, 1) for i in range(d)]
    heapq.heapify(heap)
    a1 = sum(1.0/x for x in p)
    a2 = sum(1.0/(x*x) for x in p)
    s_c1 = 0.0
    s_c2 = 0.0
    s_q2 = 0.0
    for N in range(1, max_n+1):
        _, i, k = heapq.heappop(heap)
        m[i] += 1
        heapq.heappush(heap, (-p[i]/(k+1), i, k+1))
        t = [m[j]-N*p[j] for j in range(d)]
        c1 = (1.0-a1)/12.0 - 0.5*sum((u*u+u)/p[j] for j, u in enumerate(t))
        c2 = (1.0/6.0)*sum(b3(t[j]+1.0)/(p[j]*p[j]) for j in range(d))
        q2 = c2 + 0.5*c1*c1
        s_c1 += c1
        s_c2 += c2
        s_q2 += q2
    pred_c1 = -(d-1)*(3*d+4)/24.0
    pred_c2 = d*(d-1)*(d+2)/48.0
    pred_q2 = (a2/1440.0 + a1/720.0
               + (45*d**4+150*d**3-5*d**2-238*d+36)/5760.0)
    print(f"Nmax={max_n}")
    print(f"mean c1  = {s_c1/max_n:.12f}; prediction = {pred_c1:.12f}")
    print(f"mean c2  = {s_c2/max_n:.12f}; prediction = {pred_c2:.12f}")
    print(f"mean Q2  = {s_q2/max_n:.12f}; prediction = {pred_q2:.12f}")


if __name__ == "__main__":
    check()
