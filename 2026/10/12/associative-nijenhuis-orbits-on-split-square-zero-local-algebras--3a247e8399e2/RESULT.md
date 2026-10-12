# Associative Nijenhuis orbits on split square-zero local algebras

## Finding

For every prime power \(q\) and integer \(n\ge 1\), let \(k=\mathbb F_q\), let \(V\) have dimension \(n\), and give \(A=k\oplus V\) the unital associative multiplication
\[
(a,v)(b,w)=(ab,aw+bv).
\]
Every associative Nijenhuis operator is uniquely described by
\[
N(1)=\alpha 1+u,\qquad N(v)=Tv\quad(v\in V),\qquad (T-\alpha I)u=0,
\]
where \(\alpha\in k\), \(T\in\operatorname{End}_k(V)\), and \(u\in V\). The exact number of operators is
\[
q\bigl(2q^{n^2}-q^{n(n-1)}\bigr).
\]
Under algebra automorphisms there is one orbit with \(u=0\) for each choice of \(\alpha\) and similarity class of \(T\). For each *distinct* Jordan-block length \(s\) in the \(\alpha\)-primary summand of \(T\), there is exactly one further orbit. If \(c_j(q)\) counts ordinary similarity classes of \(j\times j\) matrices over \(k\), with \(c_0(q)=1\), then the total number of orbits is
\[
\boxed{\mathcal O_n(q)=q\sum_{j=0}^{n}c_j(q).}
\]
In particular, \(\mathcal O_1(q)=q(q+1)\), \(\mathcal O_2(q)=q(q+1)^2\), and \(\mathcal O_3(q)=q(q^3+2q^2+3q+1)\). The theorem additionally determines every individual orbit size, not merely the number of orbits.

## Assumptions and scope

All operators are \(k\)-linear. The associative Nijenhuis condition is
\[
N(a)N(b)=N\bigl(N(a)b+aN(b)-N(ab)\bigr)
\qquad(a,b\in A).
\]
The automorphism group is the full group of unital \(k\)-algebra automorphisms; it is naturally \(\mathrm{GL}(V)\). No restriction is imposed on the characteristic, and \(T\) need not be nilpotent, semisimple, or diagonalizable. This statement is a classification for a specified family of local algebras; it does not classify Nijenhuis operators on all finite-dimensional associative algebras.

For a fixed pair \((\alpha,T)\), let \(\lambda\) be the partition of Jordan-block sizes in the primary summand corresponding to the linear polynomial \(t-\alpha\). Write \(b_j=\#\{\text{blocks in }\lambda\text{ of size at least }j+1\}\) for \(j\ge0\). If there is no \(\alpha\)-primary summand, the only allowed \(u\) is zero.

## Proof

**Operator normal form.** Write arbitrary \(N(1)=\alpha 1+u\) and \(N(v)=f(v)1+Tv\) for a linear functional \(f:V\to k\). Substitute \(a=b=v\in V\) into the Nijenhuis identity, using \(v^2=0\). Comparison of scalar coefficients gives \(f(v)^2=2f(v)^2\), hence \(f(v)^2=0\) and therefore \(f(v)=0\), in every characteristic. Thus \(N(V)\subseteq V\). Substitution of \(a=b=1\) then gives \(Tu=\alpha u\). These conditions are also sufficient: the pairs \((1,1)\), \((1,v)\), and \((v,w)\), for \(v,w\in V\), generate all pairs bilinearly; substitution in each pair verifies the identity. The resulting parametrization is unique.

**Operator count.** For a fixed \(\alpha\), the case \(u=0\) permits all \(q^{n^2}\) endomorphisms \(T\). For any of the \(q^n-1\) nonzero choices \(u\), the equation \(Tu=\alpha u\) imposes exactly \(n\) independent linear conditions on the \(n^2\) matrix entries, giving \(q^{n(n-1)}\) choices. Summing over the \(q\) values of \(\alpha\) yields the stated formula.

**Automorphisms and individual orbits.** The nilradical of \(A\) is exactly \(V\); each unital \(k\)-algebra automorphism restricts to an arbitrary member of \(\mathrm{GL}(V)\), and no other automorphisms exist. Conjugation sends \((\alpha,T,u)\) to \((\alpha,gTg^{-1},gu)\). Once a representative \(T\) of a similarity class is fixed, the remaining action on eigenvectors is that of \(C_{\mathrm{GL}(V)}(T)\).

Put \(S=T-\alpha I\) and \(K_j=\ker S\cap\operatorname{im}S^j\). The primary decomposition reduces the eigenvector kernel and its centralizer action to the \(\alpha\)-primary module \(\bigoplus_i k[t]/(t^{\ell_i})\). Its socle \(\ker S\) has a basis of the terminal vectors of the Jordan blocks. The filtration \(K_j\) has \(\dim K_j=b_j\). For each distinct block length \(s\), the subset \(K_{s-1}\setminus K_s\) consists of eigenvectors whose smallest occupied block length is \(s\). It is nonempty precisely when a block of length \(s\) occurs, and has cardinality \(q^{b_{s-1}}-q^{b_s}\).

The invertible module endomorphisms commute with \(S\) and act transitively on this subset: invertible changes of the equal-length summands select one nonzero terminal basis vector of length \(s\); elementary module homomorphisms from that summand to every longer summand remove the other occupied terminal coefficients. Such elementary modifications are invertible because they can be chosen triangular with identity diagonal. Conversely, \(K_j\) is invariant under every commuting invertible map, so distinct length strata cannot mix. The zero vector forms one further orbit. Thus if \(\lambda\) has \(d(\lambda)\) distinct part sizes, there are exactly \(1+d(\lambda)\) orbits for this \((\alpha,T)\). Moreover the orbit with vector zero has size
\[
\frac{|\mathrm{GL}_n(q)|}{|C_{\mathrm{GL}_n(q)}(T)|},
\]
while the orbit associated with length \(s\) has size
\[
\frac{|\mathrm{GL}_n(q)|}{|C_{\mathrm{GL}_n(q)}(T)|}
\bigl(q^{b_{s-1}}-q^{b_s}\bigr).
\]
These formulas are effective because \(T\) is given in rational canonical form and its centralizer is computable as the invertible group of the finite endomorphism algebra \(\operatorname{End}_{k[t]}(V_T)\). More explicitly, if the primary partition of \(T\) for a monic irreducible \(f\) of degree \(d_f\) has multiplicities \(m_r(f)\) of blocks of length \(r\), with conjugate partition \(\lambda_f'\), then
\[
|C_{\mathrm{GL}_n(q)}(T)|
=\prod_f q^{d_f\sum_j(\lambda'_{f,j})^2}
\prod_{r\ge1}\prod_{h=1}^{m_r(f)}(1-q^{-d_fh}).
\]
The complete expression is a positive integer.

**Orbit generating function.** The ordinary similarity-type series is
\[
C_q(z)=\sum_{n\ge0}c_n(q)z^n
=\prod_{d\ge1}\prod_{r\ge1}(1-z^{dr})^{-I_q(d)},
\]
where \(I_q(d)=d^{-1}\sum_{e\mid d}\mu(e)q^{d/e}\) is the number of monic irreducible polynomials of degree \(d\). For fixed \(\alpha\), distinguish the linear primary factor \(t-\alpha\). The ordinary partition factor is \(P(z)=\prod_{r\ge1}(1-z^r)^{-1}\). Giving each partition the weight \(1+d(\lambda)\) changes that factor to
\[
P(z)+\sum_{s\ge1}z^sP(z)=\frac{P(z)}{1-z},
\]
because partitions containing at least one part \(s\) have generating series \(z^sP(z)\). Hence for each \(\alpha\), the weighted similarity series is \(C_q(z)/(1-z)\). Summing over all \(q\) possible values yields
\[
\sum_{n\ge0}\mathcal O_n(q)z^n=\frac{qC_q(z)}{1-z},
\]
whose coefficient is \(q\sum_{j=0}^n c_j(q)\), as claimed. The \(n=0\) coefficient is an auxiliary boundary case; the theorem concerns \(n\ge1\).

## Verification

The accompanying standard-library program `verify.py` implements arithmetic in \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), exhaustively checks the Nijenhuis identity on every linear map for the tested dimensions, traverses every automorphism orbit and its size, and independently enumerates ordinary matrix similarity classes for the generating-function comparison. Run `python3 verify.py` from the extracted package. The checks cover \((q,n)=(2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3)\) and end with `VERIFY_OK`. Enumerations do not establish the general theorem; the preceding proof establishes the quantifiers for all prime powers and dimensions.

## Relationship to prior work

The associative Nijenhuis condition and its links to deformed products are developed by Uchino [1] and earlier work of Cariñena–Grabowski–Marmo [2]. The 2023 preprint of Zou–Gao–Kang–Lü [3] gives operator classifications in dimensions at most three over \(\mathbb C\); in particular, low-dimensional complex parametrizations must not be represented as new here. The enhanced adjoint-action literature [4] studies the underlying matrix-plus-vector action, and classical rational canonical theory supplies the similarity enumerator and centralizer machinery. What is asserted here is the finite-field, all-dimensional Nijenhuis-to-eigenvector characterization together with its explicit full automorphism-orbit census and orbit-size formula. The classical linear-algebra ingredients themselves are not claimed as discoveries.

## Limitations

No independent audit has been performed. Novelty comparisons remain subject to a possible earlier equivalent operator classification under different terminology, especially one using enhanced representations or pointed modules. The general formulas require the algebra to be the split unital square-zero extension of a finite field and do not extend automatically to non-split or higher-Loewy-length rings. Finite checks are corroboration, not substitutes for the arbitrary-characteristic proof.

## References

1. K. Uchino, *Twisting on associative algebras and Rota-Baxter type operators*, arXiv:0710.4309 (first public 2007-10-23), https://arxiv.org/html/0710.4309v8 .
2. J. F. Cariñena, J. Grabowski, G. Marmo, *Quantum bi-Hamiltonian systems*, International Journal of Modern Physics A 15 (2000); arXiv:math-ph/0610011 (posted 2006-10-06), https://arxiv.org/html/math-ph/0610011v1 .
3. X. Zou, X. Gao, C. Kang, J. Lü, *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras*, arXiv:2308.12121 (first public 2023-08-23), https://arxiv.org/html/2308.12121v3 .
4. K. Nishiyama and T. Ohta, *Enhanced adjoint actions and their orbits for the general linear group*, arXiv:1703.08641 (first public 2017-03-25), https://arxiv.org/abs/1703.08641 .
