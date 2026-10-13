# Prime support completely classifies directed-cycle compactness
## Finding

For every integer
\[
n\ge2,
\]
let \(C_n\) be the directed cycle of length \(n\), and let
\[
\operatorname{rad}(n)=\prod_{p\mid n}p
\]
be its square-free kernel. Then, over \(\mathsf{ZF}\),
\[
\boxed{
K_{C_n}\ \longleftrightarrow\
\bigwedge_{\substack{p\mid n\\p\ {\rm prime}}}K_{C_p}.
}
\]
Thus
\[
K_{C_n}\longleftrightarrow K_{C_{\operatorname{rad}(n)}},
\qquad
K_{C_{p^e}}\longleftrightarrow K_{C_p}.
\]
Assuming \(\mathsf{ZF}\) is consistent,
\[
\boxed{
\mathsf{ZF}+K_{C_m}\vdash K_{C_n}
\quad\Longleftrightarrow\quad
\operatorname{rad}(n)\mid\operatorname{rad}(m).
}
\]
Consequently, for every \(N\ge2\),
\[
\boxed{
\operatorname{AC}(N)\ \longleftrightarrow\
\bigwedge_{\substack{p\le N\\p\ {\rm prime}}}K_{C_p}.
}
\]

## Assumptions and scope

For a finite constraint library \(\mathcal D\), \(K_{\mathcal D}\) is the compactness statement that any \(\mathcal D\)-instance whose finite induced subinstances admit homomorphisms to \(\mathcal D\) itself admits such a homomorphism.

The directed cycle is
\[
C_n=\left(\mathbb Z/n\mathbb Z,\{(x,x+1):x\in\mathbb Z/n\mathbb Z\}\right).
\]

The source proves that \(K_{C_n}\) is equivalent over \(\mathsf{ZF}\) to the statement that every disjoint union of directed \(n\)-cycles admits a homomorphism to \(C_n\). A homomorphism from one directed \(n\)-cycle to \(C_n\) is exactly a phase choice.

The consistency qualification is needed only for the negative implication direction. The positive equivalences are theorems of \(\mathsf{ZF}\).

## Proof

Write \(\mathsf T(n)\) for phase choice on arbitrary disjoint unions of directed \(n\)-cycles. By the source's Lemma 39,
\[
K_{C_n}\longleftrightarrow\mathsf T(n).
\]

### Divisor descent

Suppose
\[
d\mid n,\qquad n=dr,
\]
and assume \(\mathsf T(n)\).

For each directed \(d\)-cycle \(X\) with successor \(s\), replace it by
\[
X\times\{0,\ldots,r-1\}
\]
with successor
\[
(x,j)\longmapsto
\begin{cases}
(x,j+1),&j<r-1,\\
(s(x),0),&j=r-1.
\end{cases}
\]
This is a directed \(n\)-cycle. Applying \(\mathsf T(n)\) to all expanded components gives a phase. The unique phase-zero vertex in an expanded component has the form \((x,j)\); its first coordinate \(x\) canonically supplies an origin for the original \(d\)-cycle. Therefore
\[
\mathsf T(n)\Longrightarrow\mathsf T(d),
\]
so
\[
d\mid n\Longrightarrow K_{C_n}\Longrightarrow K_{C_d}.
\]

### Product assembly

Assume \(\mathsf T(a)\) and \(\mathsf T(b)\), with
\[
a,b\ge2.
\]
Let \(X\) be a directed \(ab\)-cycle with successor \(s\). Define
\[
x\sim y
\quad\Longleftrightarrow\quad
y=s^{kb}(x)
\]
for some \(0\le k<a\). Every equivalence class has \(a\) points, and the quotient under the successor induced by \(s\) is a directed \(b\)-cycle.

For a family of \(ab\)-cycles, apply \(\mathsf T(b)\) to the family of quotient cycles. In each quotient component, the phase-zero class is selected. On that selected class, \(s^b\) is the successor of a directed \(a\)-cycle. Apply \(\mathsf T(a)\) to these selected \(a\)-cycles. The chosen phase-zero point then determines a phase of the original \(ab\)-cycle.

Hence
\[
K_{C_a}\wedge K_{C_b}\Longrightarrow K_{C_{ab}}.
\]
No coprimality assumption is used.

### Prime support

Factor
\[
n=\prod_{i=1}^{t}p_i^{e_i}
\]
with distinct primes \(p_i\). Divisor descent gives
\[
K_{C_n}\Longrightarrow\bigwedge_{i=1}^{t}K_{C_{p_i}}.
\]
Repeated product assembly gives the converse, since the same compactness principle may be applied repeatedly. Thus
\[
K_{C_n}\longleftrightarrow\bigwedge_{p\mid n}K_{C_p}.
\]

### Exact implication criterion

If
\[
\operatorname{rad}(n)\mid\operatorname{rad}(m),
\]
then every prime divisor of \(n\) divides \(m\), so the prime-support theorem gives
\[
K_{C_m}\Longrightarrow K_{C_n}.
\]

Conversely, suppose a prime \(p\mid n\) does not divide \(m\). The source proves that the conjunction of all prime-cycle principles other than \(K_{C_p}\) does not imply \(K_{C_p}\). Since \(K_{C_m}\) is equivalent to a conjunction of prime-cycle principles whose primes are all different from \(p\), it cannot imply \(K_{C_n}\), because divisor descent would then imply \(K_{C_p}\).

This proves the exact criterion, subject to the source's consistency hypothesis for the separation.

### Prime basis for finite choice

The source's Theorem 42 gives
\[
\operatorname{AC}(N)\longleftrightarrow\bigwedge_{i=2}^{N}K_{C_i}.
\]
Replacing each \(K_{C_i}\) by its prime-support conjunction, the primes that occur are exactly those satisfying
\[
p\le N.
\]
Therefore
\[
\operatorname{AC}(N)\longleftrightarrow
\bigwedge_{\substack{p\le N\\p\ {\rm prime}}}K_{C_p}.
\]

## Verification

The primary source was checked at Definition 1, Definition 12, Proposition 38, Lemma 39 and its proof, Theorem 6, Theorem 42 and its proof, and Corollary 59.

Proposition 38 shows that a connected \(C_n\)-instance has either no homomorphism or exactly \(n\) homomorphisms. Lemma 39 reduces \(K_{C_n}\) to disjoint directed \(n\)-cycles. Theorem 42 identifies \(\operatorname{AC}(N)\) with the conjunction of all \(K_{C_i}\) for \(2\le i\le N\). Corollary 59 supplies the ZF prime-cycle separation used for the exact negative implication criterion.

The new argument uses only finite quotients and finite cycle expansions. No computation or experimental enumeration is involved.

## Relationship to prior work

Li, Shah, Snodgrass, Thornton, and Zhou prove a strong antichain of prime directed-cycle compactness principles and separately prove that finite choice is equivalent to the conjunction of all cycle lengths through \(N\). Their paper does not classify composite single-cycle principles by prime support.

Candidate-specific searches for prime powers, square-free kernels, divisibility, cyclic torsors, and composite directed-cycle compactness did not locate an equivalent statement. The classical finite-choice literature concerns choice from unstructured finite sets and provides independence tools, but no checked source states this phase-choice classification for directed cycles.

The theorem closes the natural gap between the source's prime antichain and its all-cycle finite-choice conjunction: composite cycle lengths introduce no generators beyond their prime divisors.

## Limitations

The theorem concerns compactness principles of single directed cycles, not arbitrary finite digraphs or arbitrary CSP templates.

The exact negative implication criterion inherits the source's consistency qualification.

The result is a structural corollary of the source's cycle normal form plus its prime separation theorem; no new symmetric-model construction is claimed.

## References

[1] Anthony Li, Ishin Shah, Matthew Snodgrass, Riley Thornton, and Rui Zhou, “Compactness principles for CSPs and the Axiom of Choice,” arXiv:2609.33873v1, first posted 27 September 2026.

[2] J. K. Truss, “Finite axioms of choice,” *Annals of Mathematical Logic* 6 (1973), 147–176.
