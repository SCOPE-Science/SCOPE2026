# Independent mathematical audit

## correctness

PASS

Identifying the plane with C gives T_+=[[1-2ia,ia],[1,0]] and T_-=conj(T_+). The period matrix is T_-^m T_+^m. For the stated companion sequence u the off-diagonal cross terms in its trace cancel, leaving |u_(m+1)|²+a²|u_(m-1)|²; its determinant is a^(2m). Independent direct multiplication in the integer polynomial variable t=ia yielded p_m(1)=-3a², -2a²-15a⁴, -a²-4a⁴-63a⁶, and -2a⁴-255a⁸ for m=1,2,3,4 respectively. Strict negativity forces a real root greater than one for every a>0. The recurrence gives u_n=1-ina-(n(n+1)/2-2)a²+O(a³) for n≥3 (base u_3, then the quadratic coefficient changes by -(n+1)); parity of the norm square makes the trace error O(a⁴). For m≥2 the trace coefficient is 4-m and the determinant is O(a⁴). The simple-root branches at 1 and 0 give the stated expansions and strict small-a stability for each fixed m≥5. The exact short-dwell polynomials check both special expansions, including absence of an a⁶ term at m=4. Realification preserves moduli, and the finitely many within-period transfers preserve exponential decay when the period map is stable.

## originality

PASS

The closest inspected sources use a frozen operator, alternate positive steps on fixed operators, use a previous-operator history term, or concern continuous-time switched systems. None supplies the exact equal-block opposite-rotation threshold under the current reflected-point evaluation. Chen–Yu is a materially plausible overlap for time-varying reflected methods, but no decisive theorem was visible in the accessible material; the pass is bounded to the distinct exact statement supported by the comparisons, not a priority certification.

## value

PASS

This gives a sharp switching timescale even where the individual fixed-operator reflected iterations are stable at small step. It shows how persistent instability for every positive step through dwell four gives way to stability for sufficiently small steps at dwell five, with a nontrivial quartic boundary case. It is a useful exact benchmark for time-varying reflected methods, not merely a fixed-mode stability example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
