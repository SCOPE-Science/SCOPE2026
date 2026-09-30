# A finite-template first-obstruction dichotomy at the first-zero LPO degree
## Finding
Let \(\sigma\) be a finite relational signature in which every relation symbol has positive arity, and let \(\mathbf B\) be a fixed finite nonempty \(\sigma\)-structure. For a countable \(\sigma\)-structure \(\mathbf A\) on \(\mathbb N\), write \(\mathbf A_n\) for its induced substructure on \(\{0,\ldots,n\}\). Define \(\mathrm{FCSP}_{\mathbf B}(\mathbf A)\) to be \(0\) if every \(\mathbf A_n\) admits a homomorphism to \(\mathbf B\), and otherwise to be \(m+1\), where \(m\) is the least index for which \(\mathbf A_m\) has no homomorphism to \(\mathbf B\).

Define the first-zero omniscience problem \(\mathrm{LPO}_{\min}\) on functions \(p:\mathbb N\to\mathbb N\) by returning \(0\) when \(p(n)>0\) for every \(n\), and otherwise returning \(m+1\), where \(m\) is the least index with \(p(m)=0\).

Then exactly one of the following holds.

If there is \(b\in B\) such that for every relation symbol \(R\in\sigma\) of arity \(r\), the diagonal tuple \((b,\ldots,b)\) belongs to \(R^{\mathbf B}\), then \(\mathrm{FCSP}_{\mathbf B}\) is computable and is identically \(0\).

If there is no such \(b\), then
\[
\mathrm{FCSP}_{\mathbf B}\equiv_{\mathrm{sW}}\mathrm{LPO}_{\min}.
\]
Consequently,
\[
\widehat{\mathrm{FCSP}_{\mathbf B}}\equiv_{\mathrm{W}}\widehat{\mathrm{LPO}_{\min}}.
\]

## Assumptions and scope
The input \(\mathbf A\) is represented by characteristic functions for the relations of \(\sigma\), so every finite prefix \(\mathbf A_n\) can be read effectively. The template \(\mathbf B\) and the signature \(\sigma\) are fixed and finite, and \(B\neq\varnothing\).

The statement excludes function symbols, zero-ary relation symbols, empty templates, and promise classes that forbid some relational tuples. In particular, a promise that inputs are simple irreflexive graphs changes the available lower-bound construction.

## Proof
For the upper reduction, define a function \(q_{\mathbf A}:\mathbb N\to\mathbb N\) by
\[
q_{\mathbf A}(n)=
\begin{cases}
1,&\text{if }\mathbf A_n\to\mathbf B,\\
0,&\text{otherwise.}
\end{cases}
\]
Because both \(\mathbf A_n\) and \(\mathbf B\) are finite, the predicate \(\mathbf A_n\to\mathbf B\) is decidable by checking the finitely many maps from \(\{0,\ldots,n\}\) to \(B\). Hence \(q_{\mathbf A}\) is computable uniformly from \(\mathbf A\). A homomorphism from \(\mathbf A_{n+1}\) to \(\mathbf B\) restricts to one from \(\mathbf A_n\), so failure is monotone in \(n\). Therefore
\[
\mathrm{LPO}_{\min}(q_{\mathbf A})=\mathrm{FCSP}_{\mathbf B}(\mathbf A),
\]
and the output transformation is the identity. Thus \(\mathrm{FCSP}_{\mathbf B}\leq_{\mathrm{sW}}\mathrm{LPO}_{\min}\).

Assume now that no point of \(B\) lies simultaneously on every relation diagonal. Given \(p:\mathbb N\to\mathbb N\), construct a \(\sigma\)-structure \(\mathbf A^p\) on \(\mathbb N\) as follows. For each \(R\in\sigma\) of arity \(r\), set
\[
R^{\mathbf A^p}=\{(n,\ldots,n):p(n)=0\},
\]
and include no other tuples.

If \(p(i)>0\) for every \(i\leq n\), then \(\mathbf A^p_n\) has no relation tuples at all, so any map from its nonempty finite domain into the nonempty set \(B\) is a homomorphism. If \(p(m)=0\) for some \(m\leq n\), then any homomorphism \(h:\mathbf A^p_n\to\mathbf B\) would have to send \(m\) to a point \(b=h(m)\) satisfying
\[
(b,\ldots,b)\in R^{\mathbf B}
\]
for every \(R\in\sigma\), contradicting the hypothesis. Hence the least failing prefix is exactly the least zero of \(p\), and
\[
\mathrm{FCSP}_{\mathbf B}(\mathbf A^p)=\mathrm{LPO}_{\min}(p).
\]
Again the output transformation is the identity, so \(\mathrm{LPO}_{\min}\leq_{\mathrm{sW}}\mathrm{FCSP}_{\mathbf B}\).

Finally, if a point \(b\in B\) lies on every relation diagonal, the constant map with value \(b\) is a homomorphism from every \(\sigma\)-structure to \(\mathbf B\). Thus every finite prefix is satisfiable and \(\mathrm{FCSP}_{\mathbf B}\) is identically \(0\). This proves the dichotomy. Parallelization preserves Weihrauch equivalence, giving the displayed parallelized consequence.

## Verification
The proof was reconstructed in both directions with the output conventions checked explicitly. The nontrivial lower reduction uses only diagonal tuples, and the trivial branch is exactly the existence of a constant homomorphism valid for every input structure.

The included `verify.py` exhaustively checks the dichotomy for every one-point and two-point template over a signature with one unary and one binary relation. For templates with a diagonal point it checks every two-point input structure; for templates without one it checks every binary zero/nonzero pattern of length three against the lower-reduction construction. The script terminates with `VERIFY_OK`.

Edge cases covered by the proof include an empty signature, singleton templates, empty relation interpretations, and full relation interpretations. The empty-signature case falls into the computable branch vacuously.

## Relationship to prior work
BeMent, Hirst, and Wallace study a first-obstruction local graph-coloring problem and prove that, for every fixed number of colors, it is Weihrauch equivalent to their first-zero formulation of \(\mathrm{LPO}\). Their graph inputs are simple, so the lower reduction uses a finite clique obstruction.

The present result identifies the corresponding exact dichotomy for arbitrary fixed finite relational templates without a promise restricting input tuples. The decisive invariant is whether the template has a single point lying on every relation diagonal; if not, one diagonal vertex already supplies the obstruction gadget.

## Limitations
The theorem is representation-sensitive. It does not claim the same strong Weihrauch degree for the usual binary-output formulation of \(\mathrm{LPO}\); the source notes that its first-zero formulation is Weihrauch equivalent but not strongly Weihrauch equivalent to the binary-output version.

The lower reduction can fail under structural promises on inputs, including irreflexivity, because its obstruction uses diagonal tuples. Such promise classes require separate gadgets and may have different classifications.

No claim is made here for infinite templates, signatures with function symbols, zero-ary relations, or alternative encodings in which finite-prefix homomorphism is not uniformly decidable.

## References
Zack BeMent, Jeffry Hirst, and Asuka Wallace, “Reverse mathematics and Weihrauch analysis motivated by finite complexity theory,” arXiv:2105.01719v1, submitted 4 May 2021. The paper defines the first-zero form of \(\mathrm{LPO}\) and proves its Weihrauch equivalence with local fixed-\(k\) graph coloring.
