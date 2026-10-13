# Pairwise metrics forget \(2^{n-1}-1-\binom n2\) orbit dimensions in the universal \(L_1\) diversity

## Finding
Let \\(\\mathbb U_{L_1}^{\\delta}\\) denote the universal separable ultrahomogeneous \\(L_1\\) diversity constructed by Bryant, Nies, and Tupper. For an injective ordered \\(n\\)-tuple \\(\\bar a=(a_1,\\ldots,a_n)\\), there are
\\[
m_n=2^{n-1}-1
\\]
nontrivial unordered cuts of the label set \\([n]\\). Because every finite \\(L_1\\) diversity has a unique nonnegative cut-semidiversity decomposition, the automorphism orbit of \\(\\bar a\\) is encoded exactly by its cut-weight vector \\(\\lambda\\in\\mathbb R_{\\ge0}^{m_n}\\), subject only to the condition that every pair of labels is separated by positive total cut weight.

Forgetting all diversity values except pairs sends \\(\\lambda\\) to the induced metric by the linear cut map
\\[
(M_n\\lambda)_{ij}=\\sum_{S\\text{ separates }i,j}\\lambda_S.
\\]
This map has rank exactly \\(\\binom n2\\). Therefore, at every strictly positive cut-weight vector, the local fiber of the induced pairwise metric has affine dimension
\\[
\\boxed{2^{n-1}-1-\\binom n2}.
\\]
Consequently, for every \\(n\\ge4\\), a nonempty open set of labeled \\(L_1\\) metric profiles lifts to continuum many distinct automorphism orbits of injective ordered \\(n\\)-tuples in \\(\\mathbb U_{L_1}^{\\delta}\\), despite all tuples in a fiber having exactly the same pairwise distances. For \\(n=1,2,3\\) the hidden dimension is zero; it begins with \\(1,5,16,42,99,\\ldots\\) for \\(n=4,5,6,7,8,\\ldots\\).

## Assumptions and scope
The statement concerns injective ordered tuples and automorphisms of the full diversity structure, not automorphisms of its induced metric reduct. A cut is an unordered bipartition \\(S\\mid([n]\\setminus S)\\) with both sides nonempty, so complementary subsets represent the same cut.

The fiber-dimension conclusion is asserted on the strictly positive cut-weight stratum. This is enough to produce a nonempty open family of pairwise metric profiles with the stated continuum of lifts. Boundary fibers can have smaller relative dimension because some cut weights are forced to zero.

The linear-algebra facts about cut semimetrics are classical background. The contribution here is the exact orbit-fiber interpretation obtained by combining that cut geometry with the unique cut decomposition and exact ultrahomogeneity of the universal \\(L_1\\) diversity.

## Proof
Bryant--Nies--Tupper recall that a finite \\(L_1\\) diversity on a finite set \\(X\\) has a representation
\\[
\\delta(A)=\\sum_S\\lambda_S\\,\\delta_S(A),\\qquad \\lambda_S\\ge0,
\\]
where \\(\\delta_S(A)=1\\) precisely when \\(A\\) meets both sides of the cut \\(S\\mid(X\\setminus S)\\). They also recall that, unlike the metric case, this cut-semidiversity representation is unique. Choosing one representative of each complementary pair gives exactly \\(m_n=2^{n-1}-1\\) coordinates.

Their Fraïssé theorem says that the class of finite \\(L_1\\) diversities has a separable universal ultrahomogeneous limit. Hence two injective ordered \\(n\\)-tuples lie in the same automorphism orbit exactly when the labeled finite diversities they induce are identical. By uniqueness of cut decomposition, this is equivalent to equality of their cut-weight vectors. Conversely, every finite \\(L_1\\) diversity embeds in the limit, so every admissible weight vector occurs.

On a pair \\(\\{i,j\\}\\), a cut semidiversity restricts to the usual cut semimetric. Thus the induced metric is exactly \\(M_n\\lambda\\), where the rows of \\(M_n\\) are indexed by unordered pairs and its columns by nontrivial cuts, with entry one when the cut separates the pair.

There are \\(q=\\binom n2\\) rows, so \\(\\operatorname{rank}M_n\\le q\\). For \\(n\\ge3\\), let \\(c_S\\) be the cut-semimetric column for \\(S\\), with complements identified. For each pair \\(i<j\\),
\\[
2e_{ij}=c_{\\{i\\}}+c_{\\{j\\}}-c_{\\{i,j\\}},
\\]
where if a displayed set contains the chosen base label we replace it by its complement. Therefore every standard basis vector \\(e_{ij}\\) lies in the column span, so \\(\\operatorname{rank}M_n=q\\). The cases \\(n=1,2\\) are immediate. Rank-nullity gives
\\[
\\dim\\ker M_n=m_n-q=2^{n-1}-1-\\binom n2.
\\]

Now take a strictly positive weight vector \\(\\lambda\\). Every sufficiently small perturbation \\(\\lambda+v\\) with \\(v\\in\\ker M_n\\) remains positive, so the metric fiber through \\(\\lambda\\) contains a relatively open neighborhood in the affine space \\(\\lambda+\\ker M_n\\). Its local affine dimension is therefore the nullity above. Since a surjective linear map is open, \\(M_n(\\mathbb R_{>0}^{m_n})\\) is a nonempty open subset of the \\(q\\)-dimensional pairwise-coordinate space. If the nullity is positive, each such affine neighborhood contains continuum many distinct cut-weight vectors, hence continuum many distinct diversity orbits with the same metric profile.

For \\(n=4\\), write \\(c_i\\) for the four singleton cuts and \\(c_{12|34},c_{13|24},c_{14|23}\\) for the three \\(2+2\\) cuts. Directly on the six pair coordinates,
\\[
c_1+c_2+c_3+c_4=c_{12|34}+c_{13|24}+c_{14|23}.
\\]
Thus adding \\(t\\) to all four singleton-cut weights and subtracting \\(t\\) from all three \\(2+2\\)-cut weights preserves every pairwise distance. But every nontrivial cut semidiversity takes value \\(1\\) on the full four-point set, so the same perturbation changes \\(\\delta(\\{1,2,3,4\\})\\) by \\(t\\). This gives an explicit hidden diversity coordinate already at arity four.

## Verification
The bundled `verify.py` builds the cut-incidence matrix exactly for \\(1\\le n\\le8\\), computes its rational rank, and confirms
\\(
\\operatorname{rank}M_n=\\binom n2
\\)
and the stated nullity. It independently verifies the edge-basis identity for every pair through \\(n=8\\).

For \\(n=4\\), the checker constructs the integer kernel vector with coefficient \\(+1\\) on the four singleton cuts and \\(-1\\) on the three \\(2+2\\) cuts, confirms that all six pairwise coordinates vanish along this direction, and evaluates two strictly positive cut-weight vectors to verify equal pairwise metrics but different four-point diversity values. The current run reports `VERIFY_OK 118 exact assertions`.

## Relationship to prior work
Bryant--Nies--Tupper prove that finite \\(L_1\\) diversities form a Fraïssé class with a separable universal ultrahomogeneous limit, and they explicitly contrast unique cut-semidiversity decompositions with the generally nonunique cut-semimetric decompositions of finite \\(L_1\\) metrics. Bryant--Tupper had earlier established the cut-semidiversity representation and uniqueness theorem. Classical cut-cone literature already supplies the number of cut rays and the full \\(\\binom n2\\)-dimensional span of cut semimetrics.

The new point is the exact model-theoretic synthesis: cut weights are not merely coordinates for finite diversities; in the universal ultrahomogeneous limit they are complete ordered-tuple orbit coordinates. The metric reduct is therefore a linear quotient of the orbit-parameter space, with an exact generic hidden dimension \\(2^{n-1}-1-\\binom n2\\). Targeted published-finding corpus and web searches located the constituent cut-cone and Fraïssé facts but no source stating this orbit-fiber formula or the explicit arity-four orbit collapse.

## Limitations
The result is a consequence of known structural ingredients plus elementary linear algebra, so uncatalogued folklore remains a genuine originality risk. It does not classify boundary fibers where some cut weights vanish, nor does it classify automorphism orbits of the induced metric reduct itself. The word “open” refers to the image of the strictly positive cut-weight orthant in labeled pair-distance coordinates, not to all \\(L_1\\) metrics.

## References
1. David Bryant, André Nies, Paul Tupper, “Fraïssé Limits for Relational Metric Structures,” *Journal of Symbolic Logic* 86(3) (2021), 913–934. arXiv:1901.02122. DOI: 10.1017/jsl.2021.65. First submitted 2019-01-08.
2. David Bryant, Paul F. Tupper, “Diversities and the Geometry of Hypergraphs,” *Discrete Mathematics & Theoretical Computer Science* 16(2) (2014), 1–20. arXiv:1312.5408. DOI: 10.46298/dmtcs.2080.
3. Michel Deza, Monique Laurent, *Geometry of Cuts and Metrics*, Algorithms and Combinatorics 15, Springer, 1997.
