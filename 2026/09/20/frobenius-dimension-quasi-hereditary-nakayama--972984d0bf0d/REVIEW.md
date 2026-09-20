# Review: Maximum Frobenius dimension of quasi-hereditary Nakayama algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the invariant to
\[
F(A)=\sum_{i,j}\dim_k\operatorname{Hom}_A(I_i,P_j)
\]
and uses the standard interval description of indecomposable modules over a basic Nakayama algebra.

For linear Nakayama algebras, each projective contains each simple at most once, so every injective-to-projective Hom-space has dimension at most one, giving \(F(A)\le n^2\).

For cyclic quasi-hereditary Nakayama algebras, Uematsu--Yamagata's characterization, together with the explicit criterion in Marczinzik--Rubey--Stump Proposition 3.4, allows an index rotation with
\[
c_1+1=c_0+c_{c_0}.
\]
Writing \(r_i=i+c_i-1\), the Kupisch inequalities make \(r_i\) nondecreasing and the projective-dimension-two equation becomes \(r_1=r_{c_0}\). This forces a plateau. Periodicity then gives \(c_0\le n\), bounds all projective and injective lengths by \(2n-1\), and hence bounds every Hom-space by two.

The critical uniqueness step was checked separately. If an injective has length \(>n\), its top lift \(x\) must satisfy both \(r_x>r_{x-1}\) and \(r_x\ge x+n\). The plateau rules this out for \(2\le x\le c_0\), while \(r_x\le r_n=c_0+n-1<x+n\) rules it out for \(x>c_0\). Thus every long injective has top \(S_1\). A projective containing two eligible occurrences of \(S_1\) must then be \(P_1\), and the source must be the unique injective \(I_R=P_1\) ending at the plateau endpoint \(R=r_1\). Hence at most one of the \(n^2\) Hom-spaces can have dimension two.

The family with Kupisch series
\[
[n,2n-1,2n-2,\ldots,n+1]
\]
satisfies the projective-dimension-two criterion and has every injective-projective Hom-space nonzero, with exactly one of dimension two. Therefore it realizes \(F(A)=n^2+1\).

As a finite sanity check, the interval Hom formula and the bound were compared against direct linear-equation computations of module homomorphisms for small cyclic Nakayama modules, and exhaustive small-\(n\) Kupisch enumeration reproduces the reported maxima \(5,10,17,26,37\). These checks support but are not used in place of the general proof.

## Originality

**PASS, to the best of our knowledge.**

The motivating MathOverflow question, asked 28 January 2020, explicitly lists the initial maxima \(5,10,17,26,37,50,65\), conjectures \(n^2+1\), and currently has no posted answer. Searches for the exact formula, the title of the question, “Frobenius dimension” together with “quasi-hereditary Nakayama,” and synonymous nearly-Frobenius terminology did not locate a later solution.

The 2021 Marczinzik--Rubey--Stump paper supplies the quasi-hereditary and projective-dimension criteria used in the proof but does not study Frobenius dimension. Later work on quasi-hereditary Nakayama algebras located in the search concerns global dimension, S-connectedness, and quasi-hereditary orderings rather than this extremal invariant.

The 2026 preprint *Bounds on Frobenius dimension* (arXiv:2607.15999) is the most relevant unresolved literature risk because it directly studies the same invariant. Its available abstract states a general upper bound in terms of vector-space dimension and computations for low-dimensional and truncated path algebras; targeted searches did not surface the \(n^2+1\) quasi-hereditary Nakayama result. The full text was not inspected in this review, so a hidden specialization or equivalent statement remains possible.

## Value

**PASS.**

The result proves the exact extremal formula conjectured in an unanswered 2020 representation-theory question for every \(n\ge2\). The proof also supplies an explanatory structural mechanism: a projective-dimension-two simple creates a plateau in the cyclic endpoint function, and that plateau permits only one multiplicity-two injective-projective Hom-space. The extremal family is explicit.

## Scope and limitations

The theorem is stated for connected basic finite-dimensional Nakayama algebras over an algebraically closed field, the standard setting for the cited Kupisch-series classification. It does not claim a Morita-invariant maximum over arbitrary non-basic representatives, and it does not resolve Question 1 of the MathOverflow post concerning \(F(A)\ge\operatorname{gldim}(A)\).

Originality remains qualified to the best of our knowledge, with arXiv:2607.15999 the principal source not inspected in full.
