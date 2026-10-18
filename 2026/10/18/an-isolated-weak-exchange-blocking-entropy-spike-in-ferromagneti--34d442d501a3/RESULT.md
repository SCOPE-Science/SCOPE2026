# An isolated weak-exchange blocking entropy spike in ferromagnetic second-neighbor Ising chains

## Finding
For every periodic Ising ring of length \(n\ge6\), let \(B_n(r)\) count configurations for which no exchange of *adjacent unequal spins* strictly reduces the Hamiltonian \(H_r=-J\sum_i s_i s_{i+1}-Jr\sum_i s_i s_{i+2}\), where \(J>0\) and \(r>0\). A zero-energy exchange is **allowed** by this definition; the configuration need not be dynamically absorbing. Then \(h(r)=\lim_{n\to\infty}n^{-1}\log B_n(r)\) exists for every \(r>0\) and has the exact five-regime classification
\[
 e^{h(r)}=\begin{cases}
 \rho_0,&0<r<\tfrac12,\\
 \rho_0,&r=\tfrac12,\\
 \rho_-,&\tfrac12<r<1,\\
 \rho_*,&r=1,\\
 \rho_+,&r>1.
 \end{cases}
\]
The four positive growth constants are the largest positive real roots of, respectively,
\[
\begin{aligned}
p_0(x)&=x^6-x^5-x^4-x^2+1,\\
p_-(x)&=x^5-x^4-x^2-x-1,\\
p_*(x)&=x^9-2x^8+x^7-x^6-x^4+x^3-x+1,\\
p_+(x)&=x^9-2x^8+x^7-x^6+x+1.
\end{aligned}
\]
Numerically \(\rho_0=1.7142853291\ldots\), \(\rho_-=1.6851371102\ldots\), \(\rho_*=1.8023925656\ldots\), and \(\rho_+=1.7212355705\ldots\). In particular,
\[
\rho_*>\rho_+>\rho_0>\rho_->1,
\]
so **equal positive nearest- and next-nearest-neighbour couplings have a strict isolated maximum of weak-blocking entropy over all positive ratios**.

There is a second, different boundary phenomenon: for every \(n\ge6\),
\[
B_n(\tfrac12)-B_n(\tfrac14)=1+(-1)^n.
\]
Thus the half-coupling transition adds exactly two configurations to each even ring and none to an odd ring, without changing the thermodynamic entropy. The equal-coupling transition changes the exponential growth constant.

## Assumptions and scope
Spins \(s_i\in\{-1,+1\}\) are labelled on the cyclic sites \(i\in\mathbb Z/n\mathbb Z\); each configuration and its global spin reversal are counted separately. The second-neighbour sum counts each undirected distance-two bond once for \(n\ge6\). Ratios are fixed independent of \(n\). No restriction on total magnetization is imposed; the result is an all-magnetization count, not a fixed-density microcanonical count. An exchange of equal spins leaves the configuration unchanged; only unlike adjacent spins matter. A weakly blocked configuration is a local energy minimum under one such exchange, with energy-neutral exchanges admissible. It is not necessarily a zero-temperature terminal state when neutral events occur.

## Proof
**1. Six-spin energy test.** Write six consecutive spins as \((a,b,c,d,e,f)=(s_{i-2},s_{i-1},s_i,s_{i+1},s_{i+2},s_{i+3})\). Directly canceling unchanged bonds in \(H_r\) gives the exact energy difference between the exchanged and initial configurations:
\[
\frac{H_r(s^{i\leftrightarrow i+1})-H_r(s)}J
=(c-d)\bigl[(1-r)(b-e)+r(a-f)\bigr].
\]
Consequently one-step weak blocking is equivalent to the nonnegativity of this expression at every location. Its sign for a fixed six-spin word can change as \(r>0\) varies only at \(r=\tfrac12\) or \(r=1\): both differences in brackets lie in \(\{-2,0,2\}\), and the only positive zeros of a nonidentically-zero resulting linear expression are these two ratios. The five displayed regimes therefore exhaust all positive couplings.

**2. Exact transfer representation.** Index a zero-one matrix \(T_r\) by the 32 five-spin words \(u=(u_1,\ldots,u_5)\in\{-1,+1\}^5\). For each \(z\in\{-1,+1\}\) set \(v=(u_2,u_3,u_4,u_5,z)\), and put \((T_r)_{u,v}=1\) exactly when
\[
(u_3-u_4)\bigl[(1-r)(u_2-u_5)+r(u_1-z)\bigr]\ge0;
\]
all other entries vanish. A cyclic closed walk of length \(n\ge6\) uniquely identifies an admissible labelled spin word, and vice versa. This yields the **finite-volume identity** \(B_n(r)=\operatorname{tr}(T_r^n)\), not merely an asymptotic correspondence.

**3. Exact characteristic polynomials.** Simultaneous reversal of every spin commutes with \(T_r\). To block-diagonalize it, select the 16 five-spin representatives whose first coordinate is \(-1\), and let \(\bar v\) denote coordinatewise sign reversal of \(v\). The two explicit matrices
\[
(Q_r^\pm)_{u,v}=(T_r)_{u,v}\pm(T_r)_{u,\bar v}
\]
act on the symmetric and antisymmetric reversal sectors. Direct symbolic determinants, reproducible from the entry formula with `verification.py`, are
\[
\begin{array}{c|c|c}
 r&\det(xI-Q_r^+)&\det(xI-Q_r^-)\\ \hline
(0,1/2)&x^{10}p_0(x)&x^{10}(x^6-x^5+x^4-x^2-1)\\
1/2&x^9(x-1)p_0(x)&x^9(x+1)(x^6-x^5+x^4-x^2-1)\\
(1/2,1)&x^{10}(x-1)p_-(x)&x^{10}(x+1)(x^5-x^4+x^2-x-1)\\
1&x^7p_*(x)&x^7(x^9-x^7+x^6-3x^4-x^3+x+1)\\
(1,\infty)&x^7p_+(x)&x^7(x^9-x^7+x^6-2x^4-x+1).
\end{array}
\]
These are finite polynomial identities for explicitly defined 16-by-16 integer matrices; the attached standalone checker constructs both blocks and tests their exact symbolic determinants. Their characteristic identities also prove the half-coupling parity formula: the half-coupling eigenvalue multisets are obtained from the lower-regime ones by adding eigenvalues \(+1,-1\) while replacing two zero eigenvalues. Hence the trace differences at positive integer powers are exactly \(1+(-1)^n\).

**4. Perron growth and the isolated maximum.** Exact directed-graph decomposition of \(T_r\) gives one unique dominant strongly connected component of sizes 22, 22, 22, 32, and 28 across the five regimes; all remaining components have at most two vertices. Each dominant component has a self-loop and is therefore primitive. Its eigenvalue \(\rho>1\) is simple and strictly dominates every other eigenvalue in modulus; the smaller components have spectral radius at most one. Global spin reversal preserves the unique dominant component. Its strictly positive Perron vector is reversal-invariant, so its eigenvalue appears in \(Q_r^+\). The characteristic factorizations and exact real-root isolation therefore identify it with the stated largest positive root of \(p_0,p_-,p_*,p_+\), respectively. Perron-Frobenius theory then yields \(B_n(r)\sim\rho(r)^n\), with multiplicative constant one.

For \(r=1\), every edge permitted by \(T_{3/4}\) or \(T_2\) remains permitted, and in each comparison extra edges appear (56 versus 52 permitted arrows). Since \(T_1\) is irreducible, strict Perron monotonicity shows \(\rho_*>\rho_-\) and \(\rho_*>\rho_+\). Exact real-root isolation of the explicit polynomials gives \(\rho_0\in(1.71428,1.71429)\), \(\rho_-\in(1.68513,1.68515)\), \(\rho_*\in(1.80239,1.80240)\), and \(\rho_+\in(1.72123,1.72124)\). This proves the stated full strict ordering, including the comparison with \(\rho_0\), and finishes the proof.

## Verification
Run `python verification.py` using Python 3 and SymPy. Its tests construct the transfer and reversal-block matrices from the six-spin rule; symbolically verify all ten characteristic polynomials; identify the dominant strongly connected components; certify distinct Perron-root intervals by exact real-root isolation; and compare \(\operatorname{tr}(T_r^n)\) against a *separate full-Hamiltonian spin-swap enumeration* for every \(n=6,\ldots,12\) and all five regimes. The program also checks the exact energy-change identity over all six-spin patterns at five couplings, and the half-coupling parity identity for \(n=6,\ldots,25\). In the completed run these checks returned `ALL CHECKS PASS`. Finite enumerations corroborate, but do not replace, the uniform mathematical derivations above.

Illustrative independent exact counts \(B_6,B_8,B_{10}\) are \((32,70,232)\) for \(r=1/4\), \((34,72,234)\) for \(r=1/2\), \((34,68,194)\) for \(r=3/4\), \((46,100,364)\) for \(r=1\), and \((34,84,234)\) for \(r=2\).

## Relationship to prior work
Gómez Albarracín, Rosales and Grynberg [1] studied **this same ferromagnetic \(J_1\)-\(J_2\) Kawasaki Hamiltonian**, derived the exchange energy difference and the physically distinct *kinetic metastable* families. Their Table 2 and Appendix A provide proliferation rates for states protected from eventual lowering via chains of zero-energy moves; for \(J_1=J_2>0\) that rate is approximately 1.4655. Such a class is more restrictive than states with no *immediate strictly downhill* swap, which are counted here and have rate 1.8023925... . The difference is in quantifiers over exchange paths, not merely parameter notation. Their known coupling transition values \(0,1/2,1\) are credited; these are not proposed as new.

De Smedt, Godrèche and Luck [2,3] treat the nearest-neighbor-only \(J_2=0\) Kawasaki chain, including counting questions and the role of energy-neutral updates; hence the present claim deliberately takes \(r>0\) and makes no priority claim at \(r=0\). The exact five-regime all-magnetization *one-step weak-blocking* growth constants, the isolated peak at equal positive couplings, and the even-ring two-state correction at half coupling were not established in these inspected accounts. This comparison cannot exclude differently formulated or inaccessible prior results.

## Limitations
The count sums over all magnetizations, whereas [1] primarily studies zero-magnetization kinetic sectors; fixed-magnetization entropy and dynamical sampling laws are not derived. The theorem says nothing about terminal absorbing states after energy-neutral exchanges or about escape and activation times. Numerics reported are approximations to exact polynomial roots. The literature comparison is finite and does not constitute an independent novelty certification.

## References
[1] F. A. Gómez Albarracín, H. D. Rosales, and M. D. Grynberg, *Metastable and scaling regimes of a one-dimensional Kawasaki dynamics*, arXiv:1601.04375 (first public 2016-01-18), https://arxiv.org/abs/1601.04375, especially Section III, Table 2, and Appendix A.

[2] G. De Smedt, C. Godrèche, and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465 (2002), https://arxiv.org/abs/cond-mat/0202465.

[3] G. De Smedt, C. Godrèche, and J. M. Luck, *Metastable states of the Ising chain with Kawasaki dynamics*, arXiv:cond-mat/0210477 (2002), https://arxiv.org/abs/cond-mat/0210477.
