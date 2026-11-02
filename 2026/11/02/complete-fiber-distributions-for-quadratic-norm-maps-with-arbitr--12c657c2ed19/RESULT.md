# Complete fiber distributions for quadratic norm maps with arbitrary linear perturbations

## Finding

For every prime power \(q\), let \(K=\mathbb F_{q^2}\). For \(a,b\in K\) define
\[
F_{a,b}(x)=x^{q+1}+a x^q+b x,\qquad
N_j(a,b)=\#\{y\in K:\#F_{a,b}^{-1}(y)=j\}.
\]
The complete distribution has precisely two parameter strata:

* If \(b=a^q\), then \(N_0=q^2-q\), \(N_1=1\), \(N_{q+1}=q-1\), with all remaining multiplicities zero. Consequently \(|F_{a,b}(K)|=q\).
* If \(b\ne a^q\), then \(N_0=N_2=q(q-1)/2\), \(N_1=q\), with all remaining multiplicities zero. Consequently \(|F_{a,b}(K)|=q(q+1)/2\).

Of the \(q^4\) coefficient pairs, exactly \(q^2\) satisfy the first criterion and \(q^4-q^2\) satisfy the second. This remains valid in characteristic two, even when the additive part of the map has nontrivial kernel.

## Assumptions and scope

The field size \(q\) is any prime power, including \(q=2\). The field \(K\) is the quadratic extension of \(\mathbb F_q\). Norm and trace mean
\[
\operatorname N(x)=x^{q+1},\qquad \operatorname{Tr}(x)=x+x^q.
\]
The linear perturbation is \(L(x)=a x^q+b x\), an arbitrary \(\mathbb F_q\)-linear endomorphism of \(K\): the coefficient-to-map assignment is injective because a nonzero polynomial of degree at most \(q\) cannot vanish at every one of the \(q^2\) field elements, and cardinality then gives surjectivity onto all \(q^4\) linear endomorphisms. No separability or nonsingularity hypothesis on \(L\) is made. Targets are counted in \(K\), including those with no preimages.

## Proof

**Step 1: characterizing the first stratum.** The condition \(L(K)\subseteq\mathbb F_q\) means \(L(x)^q=L(x)\) for every \(x\in K\), i.e.
\[
a^q x+b^q x^q=b x+a x^q.\]
Since the \(\mathbb F_q\)-linear maps \(x\mapsto x\) and \(x\mapsto x^q\) are linearly independent over \(K\) as polynomial functions on \(K\), this is equivalent to \(b=a^q\). In this case
\[
F_{a,a^q}(x)=\operatorname N(x+a)-\operatorname N(a).
\]
The norm has one preimage at zero and \(q+1\) preimages at each nonzero element of \(\mathbb F_q\); hence the asserted distribution and value-set size.

**Step 2: separating target cosets for the second stratum.** Assume \(b\ne a^q\). Let \(\pi:K\to K/\mathbb F_q\) be the additive quotient. By Step 1 the \(\mathbb F_q\)-linear map \(\pi L\) is nonzero. Both domain and codomain of \(\pi L\) have dimensions two and one over \(\mathbb F_q\), respectively, so \(\pi L\) is surjective with one-dimensional kernel \(U=\mathbb F_q u\), \(u\ne0\). Since \(\operatorname N(x)\in\mathbb F_q\),
\[
\pi F_{a,b}(x)=\pi L(x).
\]
Thus each of the \(q\) target cosets in \(K/\mathbb F_q\) is reached from precisely one input line \(x_t+\mathbb F_q u\); images of different lines do not collide.

**Step 3: the induced one-variable maps.** For every \(s\in\mathbb F_q\), norm polarization gives
\[
F_{a,b}(x_t+su)=F_{a,b}(x_t)+A s^2+B_t s,
\quad A=\operatorname N(u)\in\mathbb F_q^\times,\quad B_t=\operatorname{Tr}(x_tu^q)+L(u)\in\mathbb F_q.
\]
Here \(L(u)\in\mathbb F_q\), because \(u\in U\). A full target line contains \(q\) elements.

If \(q\) is odd, every quadratic \(s\mapsto As^2+B_t s\) on \(\mathbb F_q\) has exactly one singleton value and \((q-1)/2\) two-preimage values (complete the square). Summing the contributions of the \(q\) disjoint target lines gives \(N_1=q\), \(N_2=q(q-1)/2\), and hence \(N_0=q^2-N_1-N_2=q(q-1)/2\).

If \(q\) is even, the bilinear form \((x,u)\mapsto\operatorname{Tr}(xu^q)\) is nondegenerate. For fixed \(u\ne0\), the linear functional \(x\mapsto\operatorname{Tr}(xu^q)\) is nonzero and vanishes on \(U\), since \(\operatorname{Tr}(u^{q+1})=2\operatorname N(u)=0\). It therefore induces an isomorphism \(K/U\to\mathbb F_q\). Consequently \(B_t\) runs exactly once through \(\mathbb F_q\) as the input lines vary. On the unique line with \(B_t=0\), the Frobenius square map \(s\mapsto As^2\) is a permutation, producing \(q\) singleton values. On any of the other \(q-1\) lines, the nonzero linearized polynomial \(As^2+B_t s\) has kernel \(\{0,B_t/A\}\) and therefore maps two-to-one onto exactly \(q/2\) values. Thus \(N_1=q\), \(N_2=q(q-1)/2\), and \(N_0=q(q-1)/2\) also in even characteristic.

**Step 4: parameter count.** There are \(q^2\) possible values of \(a\), with exactly one \(b=a^q\) for each. Hence \(q^2\) pairs lie in the norm-translation stratum and the remaining \(q^4-q^2\) pairs lie in the two-preimage stratum. These exhaust all cases. \(\square\)

## Verification

The included standalone script `verify.py` enumerates all \(\mathbb F_p\)-linear operators on \(\mathbb F_{p^2}\) for \(p=2,3,5,7\), computes the norm and the map outputs directly, and checks each predicted multiplicity. This covers \(16+81+625+2401=3123\) maps; it is a finite consistency check, not a substitute for the proof above. To reproduce, run `python3 verify.py` with Python 3 and no third-party dependencies.

## Relationship to prior work

Mullen, Wan and Wang (2012), arXiv:1210.8119, Theorem 2.1, bound the image size of arbitrary multivariate polynomial maps; their seven-page argument does not enumerate fibers in this coefficient family. Gao and Wang (2014), arXiv:1407.5884, study value-set distributions of random and cyclotomic polynomials, not the deterministic norm-plus-linear two-stratum classification. Zheng and collaborators (2025), arXiv:2503.06640, Theorem 3.3, study functions of a rank-one trace-like linear expression under a norm equality for the coefficients; their setup does not give a full distribution for \(\operatorname N(x)+L(x)\) with arbitrary linear \(L\).

An individual special parameter choice such as \((a,b)=(0,1)\) provides at most one case, and does not entail the all-coefficients classification. The equivalence-to-classical-quadratic-map viewpoint leaves a residual risk of implicit earlier coverage in the finite-geometry literature.

## Limitations

This theorem concerns quadratic extensions and unit leading coefficient on the norm. Multiplying the entire output by a nonzero scalar and adding a constant preserves fiber profiles, but arbitrary higher-degree extensions or nonlinear perturbations are not covered. A full uniqueness-of-novelty proof is not claimed. Computational checks are finite.

## References

1. G. L. Mullen, D. Wan and Q. Wang, *Value sets of polynomial maps over finite fields*, arXiv:1210.8119v1 (first public version 2012-10-30), Theorem 2.1. https://arxiv.org/abs/1210.8119
2. Z. Gao and Q. Wang, *A probabilistic approach to value sets of polynomials over finite fields*, arXiv:1407.5884v1 (2014-07-22). https://arxiv.org/abs/1407.5884
3. *Large class of many-to-one mappings over quadratic extension of finite fields*, arXiv:2503.06640v1 (2025), Theorem 3.3. https://arxiv.org/abs/2503.06640
