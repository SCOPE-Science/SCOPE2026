# Positive critical periodic content for complete prefix-code contraction systems

## Finding
For a finite complete prefix code over a \(b\)-symbol alphabet, the lengths of its words give a natural inhomogeneous family of contraction ratios whose critical periodic content remains **strictly positive**. More precisely, take an integer \(b\ge2\), a finite complete prefix code \(C=\{c_1,\ldots,c_m\}\), a real exponent \(s>0\), and a similarity iterated function system \(\mathcal F=\{f_1,\ldots,f_m\}\) on \(\mathbb R^d\) satisfying the strong separation condition. Assume that the contraction ratio of \(f_i\) is exactly \(r_i=b^{-|c_i|/s}\). Let \(E\) be its attractor, \(T\) its inverse expanding map, and let
\[
L=\max_i|c_i|,\qquad
\delta=\min_{i\ne j}\operatorname{dist}(f_i(E),f_j(E))>0.
\]
Then \(s\) is the similarity and Hausdorff dimension of \(E\), and for every sufficiently large integer \(k\) there is a primitive periodic orbit \(\mathcal O_k\) such that
\[
\frac{b^k}{L}\le \#\mathcal O_k\le b^k,
\qquad
\eta(\mathcal O_k)\ge\delta b^{-(k-1)/s}.
\]
Here \(\eta(\mathcal O)=\min_{x\ne y\in\mathcal O}|x-y|\). Consequently the critical periodic content as defined by Kong–Wang–Yu satisfies
\[
\boxed{\mathfrak P^s(E,|\cdot|,T)\ge\frac bL\delta^s>0.}
\]
This is a constructive affirmative case of their inhomogeneous critical-content question, allowing arbitrarily many different contraction lengths.

## Assumptions and scope
A **prefix code** means that no distinct codewords are in a proper prefix relationship. It is **complete** if every infinite sequence of \(b\)-ary digits begins with exactly one codeword. Equivalently, its finite codewords are the leaves of a finite full \(b\)-ary rooted tree. In particular the Kraft equality holds:
\[
\sum_{i=1}^{m}b^{-|c_i|}=1,
\qquad \sum_{i=1}^{m}r_i^s=1.
\]
The strong separation condition means the nonempty compact pieces \(f_i(E)\) are pairwise disjoint. Since there are finitely many pieces, \(\delta>0\). The inverse map \(T\) is defined on \(f_i(E)\) as \(f_i^{-1}\); it is well-defined because of strong separation. No equal-ratio or equal-length assumption is made. The conclusion concerns the whole sequence of constructed primitive periodic orbits, not arbitrary individual periodic orbits. The statement does not assert critical-content positivity for arbitrary, non-code-derived contraction vectors.

## Proof
**1. A universal digit cycle.** Fix an integer \(k\ge1\). Choose a cyclic de Bruijn word \(B_k\) of order \(k\) over the \(b\)-letter digit alphabet. Its length is \(M=b^k\); its \(M\) cyclic length-\(k\) blocks are all distinct. In particular its primitive digit period is exactly \(M\). De Bruijn existence follows by an Eulerian circuit of the ordinary order-\((k-1)\) overlap graph.

**2. Parse at all digit positions.** Let \(J=\mathbb Z/M\mathbb Z\). At every \(j\in J\), the right-infinite periodic digit stream starting at position \(j\) begins with one and only one codeword \(c_{i(j)}\). Define a deterministic map of finite sets
\[
F(j)=j+|c_{i(j)}|\pmod M.
\]
Choose any directed cycle \(j_0,j_1,\ldots,j_{n-1}\) of this map, with pairwise distinct residues and \(j_n=j_0\). The sequence \(w_k=(i(j_0),\ldots,i(j_{n-1}))\) is a cyclic word of original IFS symbols. Its total encoded digit length \(D=\sum_{h=0}^{n-1}|c_{i(j_h)}|\) is a positive multiple of \(M\), since the residues return to their start. Therefore
\[
M\le D\le nL,
\qquad n\le M,
\qquad \frac{b^k}{L}\le n\le b^k.
\]
The second bound follows from distinctness of all residues. In particular \(n\ge2\) as soon as \(b^k>L\).

**3. Primitivity.** Suppose the cyclic original-symbol word \(w_k\) had proper period \(1\le h<n\). Repeating its first \(h\) original symbols would repeat their concatenated digit block, of positive digit length \(D'<D\). Thus the right-infinite digit sequence starting at \(j_0\) would be periodic with digit period \(D'\). But this is a shift of \(B_k^\infty\), whose least digit period is \(M\). Hence \(M\) divides \(D'\), and the deterministic parser would return to the same residue after \(h\) original symbols, contradicting the distinctness of \(j_0,\ldots,j_{n-1}\). Therefore \(w_k\) is primitive and yields an orbit with exactly \(n\) points under the original-symbol shift and under \(T\).

**4. Weighted orbit separation.** Compare two distinct shifts of \(w_k^\infty\). They begin at distinct codeword-boundary residues \(j_h,j_{h'}\) of \(B_k\). If their common original-symbol prefix has digit-length weight \(W\), the concatenated codewords give identical digit sequences of length \(W\) at these distinct residues. By the de Bruijn property the first \(k\) digits at distinct residues cannot coincide. Consequently \(W\le k-1\). With the standard IFS symbolic ultrametric, the common-prefix contraction is
\[
\prod_{a\text{ in common prefix}} r_a
=b^{-W/s}\ge b^{-(k-1)/s}.
\]
If two original symbolic sequences first differ at their next symbol, their images lie in differently indexed first-level pieces after the common-prefix similarity has been applied. Hence their Euclidean distance is at least \(\delta\) times this common-prefix contraction. It follows that \(\eta(\mathcal O_k)\ge\delta b^{-(k-1)/s}\).

**5. Critical normalization.** Combining the preceding estimates gives, for all \(k\) with \(b^k>L\),
\[
\#\mathcal O_k\,\eta(\mathcal O_k)^s
\ge \frac{b^k}{L}\delta^s b^{-(k-1)}
=\frac bL\delta^s>0.
\]
Since \(\#\mathcal O_k\ge b^k/L\to\infty\), these orbits qualify for the critical periodic-content definition in the source. This proves the claimed lower bound.

**6. Explicit unequal-ratio example.** For \(b=2\), choose the complete code \(C=\{0,10,11\}\), \(s=1/2\), and the real-line similarities
\[
f_0(x)=x/4,\qquad
f_1(x)=1/2+x/16,\qquad
f_2(x)=3/4+x/16.
\]
Their ratios are \((1/4,1/16,1/16)\); their images of \([0,1]\) are pairwise separated with minimum interval gap \(3/16\). The attractor lies in \([0,1]\), so \(\delta\ge3/16\). With \(L=2\), the general theorem gives
\[
\mathfrak P^{1/2}(E,|\cdot|,T)\ge\left(\frac3{16}\right)^{1/2}=\frac{\sqrt3}{4}.
\]

## Verification
The standalone standard-library Python script `artifacts/verify_prefix_content.py` constructs de Bruijn digit cycles, parses their deterministic prefix-code cycles, checks the exact period and the distinct length-\(k\) factors, and tests the weighted common-prefix estimate and orbit-size inequality. It checks three complete prefix codes, including binary codeword lengths \((1,2,2)\) and \((1,2,3,3)\), and ternary lengths \((1,1,2,2,2)\). It prints `VERIFY_OK` on success. This bounded computation checks representative finite cases only; the all-orders assertion is proved above using de Bruijn uniqueness and the finite functional-graph cycle argument.

## Relationship to prior work
Kong, Wang and Yu (2026) introduce periodic separation dimension and critical periodic content. They prove equality of periodic separation dimension and Hausdorff dimension for strongly separated self-similar sets, establish positive critical content for homogeneous systems, and explicitly ask for inhomogeneous critical positivity (Question 5.1). Our lower bound provides a constructive inhomogeneous class tied to complete variable-length prefix codes, rather than solving the unrestricted question.

An earlier public result, *Positive critical periodic content for the \(\{\rho,\rho^2\}\) contraction pair* (2026), establishes the two-map, ratios-\((\rho,\rho^2)\) case by golden-mean constrained de Bruijn words. It does not imply the present three-or-more-map complete-code cases: deleting branches changes the similarity dimension and eliminates the critical Kraft equality. Here every ordinary de Bruijn digit cycle, parsed via any finite complete prefix code, yields the required periodic orbit; the deterministic code-boundary cycle method accommodates arbitrarily many codeword lengths.

The classical de Bruijn existence theorem and prefix-code Kraft equality are used as standard inputs; neither is claimed as new. The primary theorem's known equidistribution criterion also yields equidistribution of the constructed periodic orbit measures, as a direct corollary of the positive critical normalized separation bound, rather than a separate independent theorem.

## Limitations
The code-completeness hypothesis is essential to the present deterministic parsing argument; the proof does not cover arbitrary inhomogeneous contraction ratios or arbitrary incomplete prefix codes. The critical-content lower bound depends on geometric separation \(\delta\), not solely on the contraction ratios. Finite checker runs do not establish infinite-order uniqueness or priority. Although relevant primary work and the closest published mathematical finding were inspected in full, specialized unindexed coding/fractal papers may contain a more general result. An independent scientific audit has not been performed.

## References
1. D. Kong, Z. Wang and D. Yu, *Asymptotic separation of periodic orbits and fractal dimension*, arXiv:2609.16296v1, first posted 2026-09-14. https://arxiv.org/abs/2609.16296
2. *Positive critical periodic content for the \(\{\rho,\rho^2\}\) contraction pair* (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-positive-critical-periodic-content-for-the-rho-rho-2-contraction--f867b43e8ea4
3. N. G. de Bruijn, *A combinatorial problem*, Proc. Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764.
