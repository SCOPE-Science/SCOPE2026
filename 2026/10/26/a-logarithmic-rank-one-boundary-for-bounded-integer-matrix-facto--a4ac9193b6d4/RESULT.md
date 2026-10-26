# A logarithmic rank-one boundary for bounded integer matrix factorizations

## Finding

For an integer \(T\ge1\), let \(\tau_2(T,M)\) be the number of **ordered** pairs \((A,B)\) of \(2\times2\) integer matrices such that every entry of both matrices has absolute value at most \(T\) and \(AB=M\). Write
\[
E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
Then
\[
\boxed{\tau_2(T,E_{11})=\frac{384}{\pi^2}T^2\log T+O(T^2)}\qquad(T\to\infty).
\]
The logarithm is natural, and the implied constant is absolute. This supplies a sharp first asymptotic for a nonzero singular target in dimension two, between the quadratic scale of unimodular targets and the quartic scale of the zero target.

## Assumptions and scope

The target is exactly \(E_{11}\); entrywise height is the supremum of the absolute entries, and zero entries of the factors are allowed. No positivity or invertibility of either factor is assumed. The cutoff \(T\) is a positive integer; replacing \(T\) by its floor extends the asymptotic to real cutoffs. The primary subject is arithmetic counting of integral matrices (MSC2020 11C20).

For a nonzero primitive vector \(w=(u,v)\in\mathbb Z^2\), set \(h(w)=\max(|u|,|v|)\), and put
\[
U_T(w)=\#\{(a,b)\in\mathbb Z^2:|a|,|b|\le T,\ au+bv=1\},\quad
R_T(w)=\#\{(a,b)\in\mathbb Z^2:|a|,|b|\le T,\ au+bv=0\}.
\]
The zero-equation solutions are integer multiples of \((v,-u)\), so \(R_T(w)=2\lfloor T/h(w)\rfloor+1\).

## Proof

**Step 1: an exact disjoint-union count.** In a factorization \(AB=E_{11}\), the first column \(w\) of \(B\) is primitive because \(Aw=(1,0)^t\), and necessarily \(h(w)\le T\). If the second column of \(B\) vanishes, the first row of \(A\) has \(U_T(w)\) choices and its second row has \(R_T(w)\) choices. Thus this family has size
\[
S(T)=\sum_{\substack{w\in\mathbb Z^2\ \mathrm{primitive}\\1\le h(w)\le T}}U_T(w)R_T(w).
\]
If the second column of \(B\) does not vanish, then \(A\) is singular. Since its image contains \((1,0)^t\), its second row must vanish; equivalently, all these pairs belong to the family with the second row of \(A\) zero. By transposition and interchange of the factors, that family also has \(S(T)\) elements. The overlap, when both the second column of \(B\) and the second row of \(A\) vanish, has cardinality
\[
C(T)=\sum_{\substack{w\ \mathrm{primitive}\\1\le h(w)\le T}}U_T(w).
\]
Consequently, exactly,
\[
\tau_2(T,E_{11})=2S(T)-C(T)
=\sum_{\substack{w\ \mathrm{primitive}\\1\le h(w)\le T}}U_T(w)(2R_T(w)-1).
\]

**Step 2: uniform lattice-fiber estimates.** For every primitive \(w\) with \(1\le h(w)\le T\),
\[
U_T(w)=\frac{2T}{h(w)}+O(1),\qquad R_T(w)=\frac{2T}{h(w)}+O(1),
\]
with absolute constants. If both coordinates of \(w\) are nonzero, choose any Bézout solution \((a_0,b_0)\) of \(ua_0+vb_0=1\). Every solution is \((a,b)=(a_0+vt,b_0-ut)\), \(t\in\mathbb Z\). The bounds \(|a|,|b|\le T\) give two real intervals for \(t\), with centers \(-a_0/v\) and \(b_0/u\), separated by exactly \(1/|uv|\le1\), and radii \(T/|v|\) and \(T/|u|\). Their intersection therefore has length \(2T/h(w)+O(1)\), hence the stated integer-point count. If one coordinate vanishes, primitivity makes the other coordinate \(\pm1\), and the same bound follows directly.

It follows that
\[
S(T)=4T^2\sum_{\substack{w\ \mathrm{primitive}\\h(w)\le T}}\frac1{h(w)^2}
+O\!\left(\sum_{\substack{w\ \mathrm{primitive}\\h(w)\le T}}\left(\frac{T}{h(w)}+1\right)\right),
\quad C(T)\ll\sum_{\substack{w\ \mathrm{primitive}\\h(w)\le T}}\left(\frac{T}{h(w)}+1\right).
\]

**Step 3: count primitive square shells.** For every positive integer \(h\), exactly \(8\varphi(h)\) primitive vectors have \(h(w)=h\), including \(h=1\). Thus the displayed error sums are \(O(T^2)\), by the elementary inequalities \(\sum_{h\le T}\varphi(h)/h\le T\) and \(\sum_{h\le T}\varphi(h)\le T^2\). Moreover,
\[
\sum_{h\le T}\frac{\varphi(h)}{h^2}
=\sum_{d\le T}\frac{\mu(d)}{d^2}\sum_{j\le T/d}\frac1j
=\frac{\log T}{\zeta(2)}+O(1).
\]
The last equality follows from \(\sum_{d\ge1}\mu(d)/d^2=1/\zeta(2)\), the harmonic-sum estimate \(\sum_{j\le x}1/j=\log x+O(1)\), and absolute convergence of \(\sum_{d\ge1}\log(2d)/d^2\).

Therefore \(S(T)=32T^2\log T/\zeta(2)+O(T^2)\) and \(C(T)=O(T^2)\). Using \(\zeta(2)=\pi^2/6\) in \(2S(T)-C(T)\) gives the asserted constant \(384/\pi^2\). This completes the proof.

## Verification

The standalone file `verify.py` independently enumerates all bounded factor pairs at heights \(T=1,\ldots,6\) by solving the two row equations for every matrix \(B\). It separately evaluates the primitive-vector identity and checks all forty primitive square-shell counts of heights \(1,\ldots,40\). It uses exact integers and emits:

`VERIFY_OK heights=1..6 direct_AB_counts=6 primitive_shells=40 integer_exact=PASS finite_only=YES`

The exact factor-pair counts at heights \(1,\ldots,6\) are \(100,404,996,1844,3076,4500\). The finite tests corroborate the decomposition, not the infinite asymptotic; the preceding argument proves the latter.

## Relationship to prior work

Browning, Kalinin, Ostafe, Schindler and Wurzinger (2026) introduced the same bounded matrix divisor function and proved asymptotics for fixed nonsingular targets and the zero target, as well as general lower bounds for singular targets (Theorems 1.1, 1.4 and 1.5). Their displayed two-dimensional unimodular formula is \(192T^2/\pi^2+O(T\log T)\). The present target is neither nonsingular nor zero: the extra \(\log T\) factor resolves the first nonzero singular rank in dimension two.

Afifurrahman (2023/2024, Theorem 2.1) gave broad upper bounds for nonzero singular targets, not the present sharp constant. The elementary decomposition here gives a precise asymptotic without applying a general homogeneous-space counting theorem.

## Limitations

The theorem concerns the fixed primitive rank-one target \(E_{11}\), not all singular matrices or higher dimensions. General targets related to \(E_{11}\) by integral unimodular changes of basis need not preserve the entrywise height, so their constants cannot be inferred without further geometric analysis. The result is an asymptotic count, not an effective uniform estimate as the target varies. Exhaustive bibliographic priority beyond the inspected sources is not established.

## References

1. T. Browning, N. P. Kalinin, A. Ostafe, D. Schindler and L. Wurzinger, *The divisor function for matrices*, arXiv:2608.25078, first posted 2026-08-25. https://arxiv.org/abs/2608.25078
2. M. Afifurrahman, *Some counting questions for matrix products*, arXiv:2306.04885, first posted 2023-06-08; *Bull. Aust. Math. Soc.* 110 (2024), 32–43. https://arxiv.org/abs/2306.04885
