# Sharp two-sided annihilator profiles of finite-field cube-zero algebras

## Finding

Let \(q\) be any prime power, \(V\cong\mathbb F_q^r\), and \(W\cong\mathbb F_q^s\), with integers \(r,s\ge1\). Choose uniformly a multiplication tensor \(B:V\times V\to W\), either from all bilinear tensors (the **general** family) or from all symmetric bilinear tensors (the **commutative** family). Form the associative nilpotent algebra \(A_B=V\oplus W\) with multiplication \((v,w)(v',w')=(0,B(v,v'))\). Its cube is zero. Equivalently, unitize to the split finite local algebra \(R_B=\mathbb F_q\oplus A_B\), whose maximal ideal is \(\mathfrak m=A_B\).

Let \(T=\dim_{\mathbb F_q}\mathfrak m^2=\dim\operatorname{im} B\) and \(D=\dim_{\mathbb F_q}\operatorname{Ann}(\mathfrak m)-s\), where annihilation is two-sided in the general family. Thus \(D\) is the common left-and-right radical dimension of \(B\) (the usual radical in the symmetric family).

Write \(G_q(a,b)={a\brack b}_q\) for the Gaussian coefficient, set \(N_\mathrm{gen}(u)=u^2\) and \(N_\mathrm{com}(u)=u(u+1)/2\), and define \(H_q(m,t)=\prod_{i=0}^{t-1}(q^m-q^i)\) for \(0\le t\le m\), with \(H_q(m,t)=0\) when \(t>m\). For either family, using its respective function \(N\), the exact count of multiplication tensors with \((D,T)=(d,t)\) is

\[
F_{q,r,s}(d,t)={r\brack d}_q{s\brack t}_q
\sum_{j=0}^{r-d}(-1)^j q^{\binom j2}{r-d\brack j}_q\,
H_q\!\left(N(r-d-j),t\right),
\]

for all \(0\le d\le r\) and \(0\le t\le s\). Its probability is this integer divided by \(q^{sN(r)}\). In particular, for \(N(r)\ge s\), the exact conditional distribution at the prescribed Hilbert type \(\dim\mathfrak m/\mathfrak m^2=r\), \(\dim\mathfrak m^2=s\) is \(F_{q,r,s}(d,s)/H_q(N(r),s)\).

For \(r\to\infty\) with \(q,s\) fixed, the probability of an **excess two-sided annihilator** \(D>0\), both without conditioning and conditioned on \(T=s\), obeys the sharp laws

\[
\begin{aligned}
\Pr_{\mathrm{com}}(D>0)&\sim\frac{q^{-(s-1)r}}{q-1},&&s\ge2,\\
\Pr_{\mathrm{gen}}(D>0)&\sim\frac{q^{\,s-(2s-1)r}}{q-1},&&s\ge1.
\end{aligned}
\]

In each of these regimes, conditioned on \(D>0\), one has \(\Pr(D=1\mid D>0)\to1\), again either unconditionally or after conditioning on \(T=s\). The exceptional excess is therefore asymptotically a unique one-dimensional annihilating summand of the nilpotent ideal. The symmetric one-output case \(s=1\) is the classical single-symmetric-form regime and is not asserted to satisfy the rare-event law.

## Assumptions and scope

The parameter space is the **labeled tensor space**, with uniform coefficients in fixed bases, not the uniform distribution on algebra isomorphism classes. The general family allows noncommutative products; associativity holds because every product lies in \(W\), which annihilates \(A_B\) on both sides. The commutative family uses symmetric products even in characteristic two; no identification with alternating forms is made. The **two-sided annihilator** \(\operatorname{Ann}_{R_B}(\mathfrak m)\) has dimension \(s+D\). In the commutative family it equals the usual local-ring socle; in the noncommutative general family it need not equal either one-sided socle, which is not counted here. The exact count includes tensors whose image is a proper subspace of \(W\), whereas conditioning on \(T=s\) gives the genuine fixed Hilbert function \((1,r,s)\). No claim concerns nonsplit residue-field extensions, unbounded radical length, or uniform isomorphism-class sampling.

## Proof

**Step 1: fixed-subspace incidence.** For a fixed \(k\)-subspace \(U\subseteq V\), the condition \(U\subseteq\operatorname{rad}B\) is equivalent to the factorization of \(B\) through \((V/U)\otimes(V/U)\) in the general case, or \(\operatorname{Sym}^2(V/U)\) in the commutative case. The corresponding space of tensors has \(N(r-k)\) free input coordinates. For a prescribed \(t\)-dimensional image subspace of \(W\), the number of surjective linear maps from that input space onto the image is precisely \(H_q(N(r-k),t)\). There are \({s\brack t}_q\) image subspaces.

**Step 2: exact radical by incidence inversion.** A tensor with exact radical \(U\) is counted by inclusion-exclusion over all subspaces containing \(U\). For a codimension-zero base \(U\) of dimension \(d\), a containing subspace \(U'\) of dimension \(d+j\) appears with subspace-lattice Möbius coefficient \((-1)^jq^{\binom j2}\). There are \({r-d\brack j}_q\) such extensions. Summing the fixed-subspace counts from Step 1, then choosing \(U\) among \({r\brack d}_q\) subspaces, proves the displayed formula for \(F_{q,r,s}(d,t)\). The entire space has \(q^{sN(r)}\) tensors and the subset with \(T=s\) has \(H_q(N(r),s)\) tensors.

**Step 3: sharp rare-event estimate.** Let \(X\) count projective lines contained in \(\operatorname{rad}B\), and put \(M={r\brack1}_q=(q^r-1)/(q-1)\). Define \(c_k=N(r)-N(r-k)\). Then each fixed line lies in the radical with probability \(q^{-sc_1}\), and any two distinct lines span a two-space whose inclusion probability is \(q^{-sc_2}\). Hence \(\mu=\mathbb EX=Mq^{-sc_1}\) and the two-term Bonferroni inequalities give the explicit quantitative bound

\[
0\le\mu-\Pr(D>0)\le {M\choose2}q^{-sc_2}.
\]

Moreover, by the subspace union bound,
\[
\Pr(D\ge2)\le {r\brack2}_q q^{-sc_2}.
\]

For symmetric tensors, \(c_1=r\) and \(c_2=2r-1\). When \(s\ge2\), the relative Bonferroni error is at most \((M-1)q^{-s(r-1)}/2=O_{q,s}(q^{-(s-1)r})\); the leading expectation is \(\mu=(1-q^{-r})q^{-(s-1)r}/(q-1)\). For general bilinear tensors, \(c_1=2r-1\) and \(c_2=4r-4\). When \(s\ge1\), the relative error is at most \((M-1)q^{-s(2r-3)}/2=O_{q,s}(q^{-(2s-1)r})\); now \(\mu=(1-q^{-r})q^{s-(2s-1)r}/(q-1)\). These estimates prove both asymptotics and, using the \(D\ge2\) bound, conditional concentration at \(D=1\).

**Step 4: conditioning on the exact square layer.** Surjectivity fails only if some nonzero functional \(\ell\in W^*\), modulo scalar, annihilates \(\operatorname{im}B\). Each such failure has probability \(q^{-N(r)}\). Thus
\[
\Pr(T<s)\le {s\brack1}_q q^{-N(r)}.
\]

For fixed \(s\), the right side is superexponentially smaller in \(r\) than either rare-event probability from Step 3. Therefore conditioning on \(T=s\) changes neither sharp leading constant nor the conclusion \(\Pr(D=1\mid D>0)\to1\). On \(D=1\), selecting a complement to the canonical radical line in \(V\) exhibits a one-dimensional zero-product direct summand of the nilpotent algebra \(A_B\).

## Verification

The standalone script `checker.py` enumerates prime-field multiplication tensors, independently computes their square-image ranks and common left/right radicals by row reduction, and compares every observed pair \((D,T)\) against the exact Gaussian-binomial formula. Its preserved stdout is in `checker_output.txt`. It checked ten finite cases, totaling \(71{,}840\) tensors, with every stratum agreeing. These finite checks are not a proof over all field orders or dimensions; the proof above uses finite-field linear algebra, subspace Möbius inversion, and Bonferroni inequalities. The checker also exercises characteristic two, where symmetry must not be conflated with alternatingness.

## Relationship to prior work

Blackburn and McLean (first available 28 July 2021; later journal version 2022) analyze the numbers of isomorphism classes of finite rings, using class-two nilpotent algebras in their bounds. Their isomorphism-class growth statements do not specify the labeled joint square-image/two-sided-annihilator profile or its sharp rare-event constant. Bahturin and Olshanskii (first available 21 June 2024) establish broad genericity properties of nilpotent algebras and annihilator ideals under a different sampling of quotient ideals, but do not state the distribution for uniform fixed square-layer multiplication tensors. Calderón, Fernández Ouaridi, and Kaygorodov (2018) classify bilinear maps with radical of codimension two over an algebraically closed field, including annihilator-component decompositions; that is an equivalence classification at fixed tiny nonradical dimension, not a finite-field distribution with arbitrarily growing source dimension. Schmidt's work (2018 preprint, 2020 journal) covers rank distributions of individual symmetric forms, and informs the excluded single-output commutative boundary; it does not by itself give the common-radical/square-image joint laws for vector-valued tensors. The subspace-Möbius mechanism is classical and is not claimed as novel. The assessed contribution is its simultaneous algebra-invariant census together with the sharp, commutativity-dependent excess-two-sided-annihilator asymptotics and structural exceptional law.

## Limitations

The estimates are for fixed field order and fixed target dimension as the source dimension increases; no uniformity in simultaneously growing \(q\) or \(s\) is claimed. The count is for based tensors rather than algebra isomorphism types. The commutative case with \(s=1\) is not part of the rare-event assertion. Classical general tensor-enumeration identities might imply some finite formulas implicitly; a complete priority search of all historic bilinear-form and short-local-algebra literature has not been achieved. Independent mathematical validation has not been performed.

## References

1. S. R. Blackburn and K. R. McLean, *The enumeration of finite rings*, arXiv:2107.13215 (initial submission 2021-07-28); Journal of the London Mathematical Society 106 (2022), 3240–3262; DOI: 10.1112/jlms.12661. https://arxiv.org/abs/2107.13215
2. Y. Bahturin and A. Olshanskii, *On generic properties of nilpotent algebras*, arXiv:2406.15631 (initial submission 2024-06-21). https://arxiv.org/abs/2406.15631
3. A. J. Calderón, A. Fernández Ouaridi, and I. Kaygorodov, *Classification of bilinear maps with radical of codimension 2*, arXiv:1806.07009 (2018). https://arxiv.org/abs/1806.07009
4. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, Algebraic Combinatorics 3 (2020), 161–189; arXiv:1803.04274. DOI: 10.5802/alco.88. https://numdam.org/articles/10.5802/alco.88/
