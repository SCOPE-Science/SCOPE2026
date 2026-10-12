# Rank-one nil-clean fibers of trace-one cubic companion matrices over finite fields
## Finding
Let \(q\) be a prime power and let
\[
f(X)=X^3-X^2+c_1X+c_0\in\mathbb F_q[X].
\]
Write \(C_f\) for the companion matrix of \(f\), and define
\[
D_1(f)=\#\{E\in M_3(\mathbb F_q):E^2=E,\ \operatorname{rank}E=1,\ C_f-E\text{ is nilpotent}\}.
\]
For a monic polynomial \(g\), let
\[
\Phi_q(g)=\left|(\mathbb F_q[X]/(g))^\times\right|=q^{\deg g}\prod_{\pi\mid g}\left(1-q^{-\deg\pi}\right),
\]
where the product is over the distinct monic irreducible divisors \(\pi\) of \(g\). Then
\[
D_1(f)=\frac{\Phi_q(f)}{q-1}+\mathbf 1_{c_0=0}\frac{q\,\Phi_q(f/X)}{q-1}+\mathbf 1_{c_0=c_1=0}q^2.
\]
Thus a multiplicity question left open by qualitative nil-clean existence is governed by the cyclic-vector count of the characteristic polynomial, with two explicit lower-annihilator corrections.

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\). The claim counts only rank-one idempotent summands in nil-clean decompositions of trace-one cubic companion matrices. It does not claim the total number of nil-clean decompositions when the characteristic permits idempotents of other ranks. The companion convention is irrelevant up to similarity because the count is similarity-invariant.

## Proof
Every rank-one idempotent has the form \(E=uv^T\) with \(u\ne0\) and \(v^Tu=1\), with \((u,v)\sim(au,a^{-1}v)\) for \(a\in\mathbb F_q^\times\). The rank-one determinant update gives
\[
\chi_{C_f-E}(X)=f(X)+v^T\operatorname{adj}(XI-C_f)u.
\]
Since \(\operatorname{tr}C_f=1\) and the second characteristic coefficient is \(c_1\),
\[
\operatorname{adj}(XI-C_f)=X^2I+X(C_f-I)+(C_f^2-C_f+c_1I).
\]
Hence \(C_f-E\) is nilpotent exactly when
\[
v^Tu=1,\qquad v^TC_fu=1-c_1,\qquad v^TC_f^2u=1-2c_1-c_0. 	ag{1}
\]

For a projective line \([u]\), let \(h_u\) be the monic annihilator of \(u\) as a cyclic \(\mathbb F_q[X]\)-module vector under \(C_f\), and put \(d=\deg h_u\). The span of \(u,C_fu,C_f^2u\) has dimension \(d\). Therefore (1) has either no solution or exactly \(q^{3-d}\) solutions for \(v\), according as its prescribed moments do or do not satisfy the recurrence defined by \(h_u\).

The companion module is \(\mathbb F_q[X]/(f)\). For each monic divisor \(h\mid f\), the number of nonzero vectors having annihilator exactly \(h\) is \(\Phi_q(h)\); consequently the number of projective lines with annihilator \(h\) is \(\Phi_q(h)/(q-1)\).

If \(d=3\), then \(h_u=f\), and the three vectors \(u,C_fu,C_f^2u\) are independent, so (1) has exactly one solution. These cyclic lines contribute \(\Phi_q(f)/(q-1)\).

If \(d=2\), write \(h=X^2+aX+b\) and \(f=h(X)(X-s)\). Comparing the \(X^2\)-coefficient gives \(s=a+1\). Consistency of (1) with \(C_f^2u=-aC_fu-bu\) is
\[
(1-2c_1-c_0)+a(1-c_1)+b=0.
\]
After substituting the coefficients of \(f=h(X)(X-s)\), the left side is exactly \(s^3\). Thus \(s=0\), equivalently \(c_0=0\) and \(h=f/X\). Each such line contributes \(q\) choices of \(v\), giving \(q\Phi_q(f/X)/(q-1)\).

If \(d=1\), write \(h=X-\lambda\). Then (1) forces \(\lambda=1-c_1\) and \(c_0=-c_1^2\). Substitution into \(f(\lambda)=0\) gives \(-c_1^3=0\), hence \(c_1=c_0=0\) and \(\lambda=1\). There is one such projective line and it contributes \(q^2\) functionals. Summing the three annihilator degrees proves the formula.

## Verification
The included `verify.py` independently enumerates every rank-one idempotent and every coefficient pair \((c_0,c_1)\) over the prime fields of orders \(2,3,5,7\). For each case it tests nilpotency of \(C_f-E\) directly by cubing the matrix, and it computes \(\Phi_q\) independently by polynomial gcd counting. These finite checks are consistency tests, not a substitute for the field-uniform proof above.

## Relationship to prior work
Breaz and Modoi characterize exactly when companion matrices are nil-clean and construct decompositions with prescribed residual characteristic polynomial. Their Proposition 3 supplies existence, Theorem 5 gives the qualitative criterion, and Remark 6 explicitly notes that the resulting decompositions need not be unique. The present result refines that nonuniqueness in the first cubic trace-one slice by giving an exact rank-one decomposition fiber for every finite field and every coefficient pair.

Basnet and Bhattacharyya introduced the nil-clean index as a supremum of elementwise idempotent-fiber sizes, while later clean-index work computes global indices for several matrix rings. Those ring-level extrema do not determine the factorization-sensitive companion-matrix fiber above. Searches for companion-matrix decomposition counts, rank-one nil-clean fibers, and polynomial-totient formulations found qualitative or ring-level results but no statement implying this formula.

## Limitations
The theorem concerns rank-one idempotent summands only. In small characteristic, trace congruences can permit nil-clean decompositions with idempotents of other ranks, and those are not counted here. The computational verification covers four prime fields; extension fields are covered by the algebraic proof, not by exhaustive computation. Literature search cannot prove absolute novelty, and later work on generalized nil-clean companion decompositions remains a residual comparison risk, although the inspected results use different decomposition notions or qualitative existence statements.

## References
1. S. Breaz and G. C. Modoi, “Nil-clean companion matrices,” arXiv:1503.06668, first public 23 March 2015; Linear Algebra and its Applications 489 (2016), 50–60, DOI 10.1016/j.laa.2015.10.005.
2. D. K. Basnet and J. Bhattacharyya, “Nil clean index of rings,” International Electronic Journal of Algebra 15 (2014), 145–156, DOI 10.24330/ieja.266244.
3. B. L. Schoonmaker, “Clean Indices of Common Rings,” PhD dissertation, Brigham Young University, 2018, ScholarsArchive etd/7027.
