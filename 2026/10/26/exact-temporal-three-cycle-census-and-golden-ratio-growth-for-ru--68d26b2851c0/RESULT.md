# Exact temporal three-cycle census and golden-ratio growth for Rule 62 rings

## Finding

For each integer \(n\ge1\), let \(C_n\) count the exact least-period-three orbits of elementary cellular automaton Rule 62 with periodic spatial boundary conditions on \(n\) labeled sites. With \(\varphi=(1+\sqrt5)/2\), \(Q(t)=t^8+t^7+t^6+t^5+3t^4+2t^3+t^2+2t+1\), and the multiset \(\lambda_1,\ldots,\lambda_8\) of its complex roots, the complete enumeration is

\[
 C_n=\frac13\left(\varphi^n+(-\varphi^{-1})^n+2\cos(\pi n/2)+\sum_{j=1}^8\lambda_j^n\right).
\]

All roots of \(Q\) lie strictly inside the circle of radius \(3/2\). Consequently
\[
C_n=\frac{\varphi^n}{3}+O\bigl((3/2)^n\bigr),\qquad \lim_{n\to\infty}C_n^{1/n}=\varphi.
\]

The initial orbit counts \(C_1,\ldots,C_{12}\) are \(0,0,1,0,5,7,7,24,22,35,77,87\). These counts concern actual temporal orbits: configurations related only by a spatial rotation are not identified.

## Assumptions and scope

At each site, set the new bit by the Wolfram-code-62 local rule
\[
f(a,b,c)=\left\lfloor\frac{62}{2^{4a+2b+c}}\right\rfloor\bmod2,\qquad (a,b,c)\in\{0,1\}^3.
\]
At site \(i\in\mathbb Z/n\mathbb Z\), \((F_nx)_i=f(x_{i-1},x_i,x_{i+1})\). For \(n=1,2\), the neighborhoods are read with repetition under the same periodic-boundary definition. A three-cycle is an orbit containing exactly three different global configurations, not a spatially translated pattern or an eventual transient orbit. All counts are for \(n\ge1\), including even and odd rings.

## Proof

**Step 1: cyclic walks recognize periodic space-time constraints.** Define \(f^{[3]}:\{0,1\}^7\to\{0,1\}\) by three successive applications of \(f\) over overlapping consecutive triples of lengths \(7\to5\to3\to1\). Index 64 states by six-bit words \(u=(u_0,\ldots,u_5)\). For each \(b\in\{0,1\}\), put \(v=(u_1,\ldots,u_5,b)\) and put one directed edge \(u\to v\) precisely when
\[
f^{[3]}(u_0,\ldots,u_5,b)=u_3.\]
Let \(M\) be the resulting 64-by-64 integral adjacency matrix. A closed length-\(n\) walk is exactly a cyclic string satisfying \(F_n^3x=x\). Indeed, the overlap equations force a global cyclic assignment of the original bits; conversely every such assignment generates one closed walk with its distinguished starting spatial site. This remains valid for \(n<7\) because the walk itself forces the needed periodic repetitions. Thus \(\#\operatorname{Fix}(F_n^3)=\operatorname{tr}(M^n)\) for every \(n\ge1\).

**Step 2: subtract temporal fixed points.** Apply the same construction to the one-step local rule, this time with a 4-by-4 matrix \(H\) indexed by two-bit words and with edge \((a,b)\to(b,c)\) precisely when \(f(a,b,c)=b\). A direct exact determinant gives
\[\det(tI-H)=t^3(t-1).\]
Therefore \(\operatorname{tr}(H^n)=1\) for every \(n\ge1\). A point fixed by the third iterate has least temporal period either one or three, and each three-cycle contains three states. Hence
\[3C_n=\operatorname{tr}(M^n)-1.\]

**Step 3: exact transfer determinant.** Direct integer-polynomial elimination from the fully specified binary transition matrix yields
\[
\det(tI-M)=t^{51}(t-1)(t^2+1)(t^2-t-1)Q(t),
\]
where
\[
Q(t)=t^8+t^7+t^6+t^5+3t^4+2t^3+t^2+2t+1.
\]
The standalone `verify_rule62.py` constructs every entry of both matrices directly from the bit rule and checks these factorizations symbolically with exact integer arithmetic; it is a reproducible finite algebraic certificate rather than numerical eigenvalue matching. Since \(\operatorname{tr}(M^n)\) equals the sum of \(n\)-th powers of all 64 eigenvalues, counted with algebraic multiplicity, the roots \(1,\,i,\,-i,\,\varphi,\,-\varphi^{-1},\,\lambda_1,\ldots,\lambda_8\), and 51 zeros give the stated formula after removing the \(1\) fixed state.

**Step 4: a strict spectral gap.** Apply the rational Schur reduction to the monic polynomial \(p(z)=(2/3)^8Q(3z/2)\). For real-coefficient \(p(z)=\sum_{j=0}^ma_j z^j\), with \(|a_0|<|a_m|\), set
\[
 S(p)(z)=\frac{a_m p(z)-a_0 z^m p(z^{-1})}{z},
\]
then scale to make the new leading coefficient one. The elementary Schur--Cohn lemma (proved by applying Rouché's theorem on the unit circle to \(p\) and its reversed polynomial) says the roots of \(p\) all lie in the open unit disk if and only if the same is true of \(S(p)\). The exact-rational computations verify \(|a_0/a_m|<1\) at every degree \(8,7,\ldots,1\), hence all roots of \(Q\) have modulus strictly less than \(3/2\). The other subleading eigenvalues have moduli at most one, and therefore their summed powers contribute \(O((3/2)^n)\) in the explicit formula. Since \(\varphi>3/2\), the asserted asymptotic follows.

## Verification

Run `python verify_rule62.py` using Python 3 and SymPy. It reconstructs the two transfer matrices from the bit rule; verifies their characteristic polynomials by exact arithmetic; applies an eight-stage exact-rational Schur reduction; checks the traces and integer three-cycle counts against an independent direct brute-force global-state enumeration for \(1\le n\le12\); and prints a `VERIFY_OK` message only after every assertion passes. The finite brute-force sample is illustrative; the proof applies for every integer ring length because of the transfer-walk bijection and verified symbolic factorization.

## Relationship to prior work

Taga and collaborators (2021) establish general Koopman-cycle correspondences and compute spectra at one ring size. Zhu and Richard (2026) analyze Koopman spectra of elementary cellular automata on finite rings and document a period-three signature of Rule 62 for sampled ring lengths. Their analysis motivates asking for an all-length exact three-cycle count, but does not give this closed trace formula. Stricker (2023) classifies rules by attainable cycle lengths and tabulates finite examples, without this temporal orbit enumeration for arbitrary ring length. Chen, Shi, Chen and Jin (2012) investigate period-three Rule 62, gliders, and symbolic chaos on bi-infinite strings; a complete copy was not obtainable for statement-by-statement comparison. The result proved here concerns counts of exact temporal period-three orbits over every finite cyclic length; known existence or classification by possible orbit lengths does not imply these counts or their golden-ratio asymptotics.

## Limitations

The formula does not count or classify the other temporal periods of Rule 62, distinguish primitive spatial periods, or assert new mixing or entropy results for the bi-infinite system. It does not prove historical priority against inaccessible materials, especially the complete 2012 Chen--Shi--Chen--Jin text; an equivalent finite-ring count may exist under another name. The rate \(O((3/2)^n)\) is a certified bound, not the claimed best possible subleading exponential rate. 

## References

1. Qingying Zhu and Serge Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations*, arXiv:2610.10967v1 (first public 2026-10-07), https://arxiv.org/abs/2610.10967.
2. Hans-Peter Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, Complex Systems 32 (2023), 229–251, https://doi.org/10.25088/ComplexSystems.32.3.229.
3. Keisuke Taga, Yuzuru Kato, Yoshinobu Kawahara, Yoshihiro Yamazaki, Hiroya Nakao, *Koopman spectral analysis of elementary cellular automata*, arXiv:2106.01118 (2021), https://arxiv.org/abs/2106.01118.
4. Fangyue Chen, Lun Shi, Guanrong Chen, Weifeng Jin, *Chaos and gliders in periodic cellular automaton rule 62*, Journal of Cellular Automata 7 (2012), 287–302; bibliographic abstract https://scholars.cityu.edu.hk/en/publications/chaos-and-gliders-in-periodic-cellular-automaton-rule-62/.
