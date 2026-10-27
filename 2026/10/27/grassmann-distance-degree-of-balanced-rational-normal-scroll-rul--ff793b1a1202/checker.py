#!/usr/bin/env python3
"""Exact sample checks for projection-Grassmannian scroll-ruling critical points."""
import sympy as sp

t = sp.Symbol('t')
for m in (2, 3, 4, 5):
    s = sum(t**(2*j) for j in range(m + 1))
    q1 = [1 + j + (j*j % 5) for j in range(m + 1)]
    q2 = [1 + 2*j + (j*j % 5) for j in range(m + 1)]
    p1 = sum(c*t**j for j,c in enumerate(q1))
    p2 = sum(c*t**j for j,c in enumerate(q2))
    f = sp.expand(p1**2/sum(c*c for c in q1) + p2**2/sum(c*c for c in q2))
    H = sp.Poly(sp.expand(sp.diff(f,t)*s - f*sp.diff(s,t)),t)
    assert H.degree() == 4*m - 2, (m,'wrong degree',H.degree())
    assert sp.gcd(H,H.diff()).degree() == 0, (m,'repeated critical root')
    assert sp.gcd(H,sp.Poly(s,t)).degree() == 0, (m,'critical pole')
    # These orthogonal data planes have cut determinant proportional to p1*p2.
    assert sp.gcd(H,sp.Poly(p1*p2,t)).degree() == 0, (m,'cut critical point')
    print('VERIFY_OK', 'm='+str(m),'critical='+str(4*m-2),'squarefree','away_from_poles','away_from_cut')
