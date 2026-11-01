# Maximal-cyclic tomography on the first nonhomocyclic rank-two prime-power torus

## Finding
For each prime \(p\), let \(G=\mathbb Z/p^2\mathbb Z\times\mathbb Z/p\mathbb Z\). Record unnormalized sums of arbitrary complex functions over **one copy of every coset** of **every maximal cyclic subgroup**. The resulting maximal-cyclic Radon transform \(R\) is injective; moreover, its complete squared-singular-value spectrum is
\[
\begin{array}{c|c}
\text{squared singular value}&\text{multiplicity}\\\hline
p& p^2(p-1)\\
p^2&p^2-1\\
p^3+p^2&1.
\end{array}
\]
There are exactly \(2p\) maximal cyclic-subgroup directions, and **every one of those directions is necessary** for injectivity when all remaining cosets are kept. On the zero-mean function subspace, the unweighted condition number is \(\sqrt p\). More strongly, no positive scalar reweighting of whole direction families can improve this condition number: the sharp infimum remains \(\sqrt p\), with an explicit complete equality class described below.

## Assumptions and scope
Fix a prime \(p\ge2\), write group elements as \((x,y)\) with \(x\) modulo \(p^2\) and \(y\) modulo \(p\), and let \(\ell^2(G)\) have the usual counting inner product. A cyclic subgroup \(H\) is **maximal cyclic** if it is not strictly contained in any other cyclic subgroup of \(G\). Define \(R_Hf\), indexed exactly once by the cosets \(L\in G/H\), by
\[
(R_Hf)(L)=\sum_{x\in L}f(x),\qquad R=\bigoplus_{H\in\mathcal H}R_H.
\]
The complete maximal-cyclic direction family is
\[
\mathcal H=\{H_t=\langle(1,t)\rangle:t\in\mathbb F_p\}
\cup\{K_s=\langle(ps,1)\rangle:s\in\mathbb F_p\}.
\]
Each \(H_t\) has order \(p^2\), whereas each \(K_s\) has order \(p\). Hence there are \(p^2+p^3\) measured coset sums. The **weighted direction-family model** replaces each component \(R_{H_t}\) by \(\sqrt{\alpha_t}R_{H_t}\) and \(R_{K_s}\) by \(\sqrt{\beta_s}R_{K_s}\), where all \(\alpha_t,\beta_s\) are strictly positive reals. There are no individual-coset or frequency-dependent weights. Write \(\ell^2_0(G)=\{f:\sum_Gf=0\}\).

## Proof
**Maximal directions.** An element with unit first coordinate generates a cyclic group of order \(p^2\), normalized uniquely to \(H_t\). Every cyclic subgroup of order \(p\) has a generator of the form \((ps,0)\) or \((ps,1)\). The first kind lies inside every \(H_t\) (or equals the trivial group); each subgroup of the second kind is \(K_s\). It cannot lie in any cyclic group of order \(p^2\), because the unique order-\(p\) subgroup of any such group is \(\langle(p,0)\rangle\). The \(K_s\) are pairwise distinct. This exhausts all cyclic subgroups and proves the asserted maximality list.

**Fourier diagonalization.** The characters
\[
\chi_{k,l}(x,y)=\exp\!\left(2\pi i\left(\frac{kx}{p^2}+\frac{ly}{p}\right)\right),
\quad 0\le k<p^2,\quad 0\le l<p,
\]
are a complete orthogonal basis. Directly from the coset-sum definition, \(R_H^*R_Hf(x)=\sum_{h\in H}f(x+h)\). Thus its eigenvalue on \(\chi_{k,l}\) is \(|H|\) if the character is trivial on \(H\) and zero otherwise. The two triviality tests reduce to
\[
H_t:\ k+pl t\equiv0\pmod{p^2};\qquad
K_s:\ ks+l\equiv0\pmod p.
\]
If \(p\nmid k\), exactly one \(K_s\) annihilates the character and no \(H_t\) does, giving eigenvalue \(p\) on \(p^2(p-1)\) characters. If \(k=pa\) and \(l\ne0\), exactly one \(H_t\) annihilates it and none of the \(K_s\) does; if \(k=pa\ne0\) and \(l=0\), every \(K_s\) annihilates it and no \(H_t\) does. Both latter nonconstant cases have eigenvalue \(p^2\), on \(p(p-1)+(p-1)=p^2-1\) characters. The constant character receives \(p(p^2)+p(p)=p^3+p^2\). The multiplicities sum to \(|G|=p^3\), proving the entire spectrum and injectivity.

**Indispensability.** For each \(K_s\), choose \((k,l)=(1,-s\bmod p)\); this nonconstant character is annihilated by exactly \(K_s\). For each \(H_t\), choose \((k,l)=(-pt\bmod p^2,1)\); this nonconstant character is annihilated by exactly \(H_t\). Removing any one whole direction therefore destroys injectivity, even if every coset in every other direction is retained.

**Exact positive-weight minimax.** Put \(u_s=p\beta_s\), \(v_t=p^2\alpha_t\). The nonconstant squared singular values (with repetition) are exactly the individual \(u_s\), the individual \(v_t\), and \(\sum_su_s\). Accordingly,
\[
\kappa_0(R_{\alpha,\beta})^2=
\frac{\max\{\sum_su_s,\max_t v_t\}}
{\min\{\min_su_s,\min_t v_t\}}.
\]
Let the denominator equal \(m>0\). Every \(u_s\ge m\), so \(\sum_su_s\ge pm\), and the squared condition number is at least \(p\). Equality holds **if and only if**
\[
 u_s=m\quad\text{for every }s,\qquad m\le v_t\le pm\quad\text{for every }t,
\]
for some common \(m>0\). These weights exist (including the unweighted transform, for which \(m=p\)), so the lower bound and all equality cases are sharp. In contrast with a frequency preconditioner, a single scalar per full direction cannot eliminate the exceptional \(p-1\)-dimensional large-eigenvalue space.

## Verification
`CHECK.py` is an independent Python 3 standard-library check. Run `python3 CHECK.py` in a directory containing the file. It enumerates every cyclic subgroup (rather than taking the maximal family on faith), constructs every coset and the full integer Gram matrix, cross-checks its exact translation kernel, and exhausts character-annihilator energies and unique-direction witnesses for primes \(2,3,5,7\). Its final line is:

`VERIFY_OK four_primes=PASS direct_coset_Gram=PASS exact_abelian_Fourier=PASS witnesses=PASS weighted_spectrum=PASS`

These finite cases corroborate but do not prove the all-prime assertion. The proof above is the universal justification; the weighted optimum follows from an exact positive-sum inequality, with no numerical optimizer.

## Relationship to prior work
Ilmavirta's *On Radon Transforms on Finite Groups* (first publicly posted 2014-11-14), Section 7.3, introduces maximal cyclic geodesics and proves injectivity for the **elementary** group \(C_p\times C_p\), but does not derive the singular values, irredundancy, or scalar-weight stability of the different group \(C_{p^2}\times C_p\). Kingston and Svalbe (2005) prove Fourier-slice reconstruction for **square** cyclic grids; their published scope is distinct from this unequal-exponent group. A published study of projective cyclic Radon transforms proves a sharp scalar-weight barrier for \((\mathbb Z/N\mathbb Z)^2\), but its square-grid frequency and subgroup geometry do not imply the present nonhomocyclic result. Kumar (2020) studies the number of maximal cyclic subgroups in rank-two abelian prime groups, a group-theoretic ingredient rather than a tomography spectrum. The full text of Ilmavirta and the square-grid comparison was examined; the other two comparisons were limited to accessible abstracts/metadata, with priority risk noted below.

## Limitations
The result concerns only the group \(C_{p^2}\times C_p\), ordinary coset sums, all maximal cyclic-subgroup directions, and positive weights constant across each direction's cosets. It does not optimize arbitrary individual-coset weights or allow frequency-domain inversion filters. The stated singular values use counting inner products and unnormalized sums; alternative normalizations change numerical values. The literature comparison is bounded and independent mathematical validation has not been performed. An earlier equivalent statement in group-theoretic or imaging literature is a remaining originality risk.

## References
1. J. Ilmavirta, *On Radon Transforms on Finite Groups*, arXiv:1411.3829, first posted 2014-11-14; Section 7.3 on maximal transforms. https://arxiv.org/abs/1411.3829
2. A. Kingston and I. Svalbe, *A Discrete Modulo N Projective Radon Transform for N × N Images*, LNCS 3429 (2005), 136–147. https://doi.org/10.1007/978-3-540-31965-8_13
3. *Sharp scalar-view conditioning and a smallest-prime barrier for projective cyclic Radon transforms*, published research record, 2026. https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-scalar-view-conditioning-and-a-smallest-prime-barrier-for--58911b2d31f1/RESULT.md
4. P. Kumar, *Maximal cyclic subgroups of a finite abelian p-group of rank two*, Quasigroups and Related Systems 28 (2020), 237–242. https://www.math.md/publications/qrs/issues/v28-n2/13463/
