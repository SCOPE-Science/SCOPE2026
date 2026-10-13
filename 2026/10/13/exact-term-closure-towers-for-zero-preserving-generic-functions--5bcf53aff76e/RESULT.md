# Exact term-closure towers for zero-preserving generic functions on finite-field vector spaces

## Finding
Let \(q\) be a prime power and consider \(\mathbb F_q\)-vector spaces expanded by finitely many function symbols \(f_1,\ldots,f_s\) of positive arities \(r_1,\ldots,r_s\). Assume only that each added function preserves the all-zero tuple:
\[
f_j(0,\ldots,0)=0.
\]
Let \(F_m\) be the free algebra on \(m\ge1\) generators in this equational class. Let \(V_n\) be the vector subspace of \(F_m\) spanned by all terms whose nesting depth in the added function symbols is at most \(n\), and put \(d_n=\dim_{\mathbb F_q}V_n\). Then
\[
d_0=m,\qquad d_{n+1}=m-s+\sum_{j=1}^s q^{r_jd_n}\quad(n\ge0).
\]
Thus the entire finite-depth generated-hull profile is explicit. For one unary zero-preserving function over \(\mathbb F_2\) on one free generator,
\[
d_{n+1}=2^{d_n},\qquad d_0=1,
\]
so
\[
d_n=1,2,4,16,65536,\ldots,
\]
and \(|V_n|=2^{d_n}\). The closure stages therefore grow by a genuine power tower.

## Assumptions and scope
The statement concerns the free algebra determined by the vector-space identities together with the zero-preservation identities above; it does not assert that every finitely generated substructure in a model companion is free. Bossut's generic-function construction supplies the model-theoretic motivation: Section 5.2 constructs free amalgams after adding a generic function, Remarks 5.2.3--5.2.4 state that the same construction works for functions of arbitrary arity, and Remark 5.2.8 explicitly places generic functions over infinite-dimensional \(\mathbb F_2\)-vector spaces among the motivating examples and mentions the unary condition \(f(0)=0\).

## Proof
Set \(V_{-1}=\{0\}\), so \(d_{-1}=0\). Build the free algebra stage by stage. At stage \(0\), take a vector space with basis the \(m\) free generators. Suppose \(V_n\) has been constructed and all function values on tuples from \(V_{n-1}\) have already been assigned. For each \(j\), and for every tuple
\[
\bar v\in V_n^{r_j}\setminus V_{n-1}^{r_j},
\]
adjoin a fresh basis vector \(e_{j,\bar v}\) and define \(f_j(\bar v)=e_{j,\bar v}\). The all-zero tuple lies in \(V_{-1}^{r_j}\), so its prescribed value is already \(0\) and no basis vector is introduced for it.

Distinct pairs \((j,\bar v)\) receive distinct fresh basis vectors. This is not merely a counting convention: the resulting union has the universal property of the free algebra. Given arbitrary images of the original \(m\) generators in any target algebra satisfying the same identities, extend linearly on \(V_0\); once the map is defined on \(V_n\), send each new basis vector \(e_{j,\bar v}\) to \(f_j\) applied to the images of the coordinates of \(\bar v\). This recursively gives a unique homomorphism. Hence there are no further linear relations among the new symbols.

Therefore the number of new basis vectors at step \(n+1\) is
\[
\sum_{j=1}^s\left(|V_n|^{r_j}-|V_{n-1}|^{r_j}\right)
 =\sum_{j=1}^s\left(q^{r_jd_n}-q^{r_jd_{n-1}}\right),
\]
and
\[
d_{n+1}=d_n+\sum_{j=1}^s\left(q^{r_jd_n}-q^{r_jd_{n-1}}\right).
\]
Rearranging gives
\[
d_{n+1}-\sum_{j=1}^s q^{r_jd_n}
=d_n-\sum_{j=1}^s q^{r_jd_{n-1}}.
\]
The left side is therefore constant in \(n\). Evaluating at \(n=0\) gives \(d_0-\sum_jq^{r_jd_{-1}}=m-s\), proving
\[
d_{n+1}=m-s+\sum_{j=1}^s q^{r_jd_n}.
\]

## Verification
The accompanying `verify.py` checks the stage-count formula against the collapsed recurrence for several choices of \(q\), number of generators, and operation arities. It also checks the telescoping invariant at every constructed step. The unary binary-field specialization recovers
\[
1,2,4,16,65536
\]
for the first five dimensions. The script returns `VERIFY_OK`.

## Relationship to prior work
Bossut's 2024 preprint develops the generic-function Fraïssé construction and explicitly notes that functions of arbitrary arity may be added. It also points to infinite-dimensional \(\mathbb F_2\)-vector spaces with generic functions, and to an abelian-group example with a unary \(f\) satisfying \(f(0)=0\). The paper establishes the model-theoretic construction, not the finite-depth dimension recurrence above.

Targeted searches for the exact recurrence, for free vector spaces with a unary operation, and for term-depth growth did not locate this formula. The closest retrieved material concerned unrelated free algebras and generic-function model companions. The calculation should nevertheless be viewed as a structural consequence of the free-algebra normal form, with a residual possibility that it is folklore in universal algebra.

## Limitations
The recurrence is for the free zero-preserving expansion. Additional identities involving the \(f_j\), linearity of any \(f_j\), or accidental equations in a nonfree generated substructure can reduce the growth. The result also measures syntactic generated-hull depth, not model-theoretic algebraic closure or forking geometry.

## References
1. Yvon Bossut, *On some Fraïssé limits with free amalgamation*, arXiv:2403.07616, first submitted 12 March 2024. See Section 5.2, especially Remarks 5.2.3--5.2.4 and Remark 5.2.8.
2. Standard universal-algebra free-object construction: the proof above is self-contained and uses only the universal property of a free algebra in an equational class.
