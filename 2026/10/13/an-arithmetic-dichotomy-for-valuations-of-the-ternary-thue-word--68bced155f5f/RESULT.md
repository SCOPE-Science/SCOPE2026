# An arithmetic dichotomy for valuations of the ternary Thue word

## Finding

Let \(\mathbf t\) be the infinite fixed point beginning in \(0\) of the morphism
\[
0\mapsto012,\qquad 1\mapsto02,\qquad 2\mapsto1.
\]
For an arbitrary integer valuation \(\mathbf a=(a_0,a_1,a_2)\in\mathbb Z^3\), let \(\rho_{\mathbf a}(n)\) be the number of different values of \(\sum_{i=0}^2 a_i|u|_i\) as \(u\) ranges over **all** length-\(n\) factors of \(\mathbf t\). Let \(\rho_{\rm ab}(n)\) be the number of different Parikh vectors of these factors. Set
\[
A=a_0+a_2-2a_1,\qquad E=a_0-a_2.
\]
Then the following are equivalent:

1. \(\rho_{\mathbf a}(n)=\rho_{\rm ab}(n)\) for every integer \(n\ge1\).
2. \(A\ne0\) and \(A\nmid E\) (ordinary integer divisibility, with negative divisors permitted).

There is also a quantitative converse. If the equivalent conditions fail, let
\[
n_k=\frac{2\cdot4^k+1}{3}\qquad(k=0,1,2,\ldots).
\]
Then
\[
\rho_{\rm ab}(n_k)-\rho_{\mathbf a}(n_k)\longrightarrow+\infty.
\]
More explicitly, if \(A=0\), this deficit is at least \(k-1\). If \(A\ne0\) and \(A\mid E\), put \(h=E/A\in\mathbb Z\); the deficit is at least
\[
\max\left\{0,\left\lfloor\frac{k+2-2|h|}{2}\right\rfloor\right\}.
\]
These bounds concern the displayed subsequence, not every length.

The criterion is not a monotone condition on the spacing of the three weights. For example, \((0,2,7)\) preserves all abelian classes for every length, whereas \((0,2,8)\) does not.

## Assumptions and scope

The letters in the morphism are formal symbols \(0,1,2\); the valuation subsequently assigns arbitrary integers to them. Equal or negative weights are allowed. Adding the same constant to every weight affects all same-length sums equally and hence changes none of the counts. The usual definition for nonnegative valuations is therefore covered as a special case, after translation of the weights if necessary.

Two factors are abelian equivalent precisely when their triples of letter multiplicities coincide. Consequently \(\rho_{\mathbf a}(n)\le\rho_{\rm ab}(n)\) always. Equality of these cardinalities for a fixed length means that the weight-sum map is injective on the Parikh vectors occurring at that length.

We use the established complete Parikh-vector description from Blanchet-Sadri, Currie, Rampersad and Fox (2014), Lemma 8 and the proof of Theorem 2. For each \(n\ge1\), let \(p_n\) and \(q_n\) be the minimum and maximum numbers of symbols \(1\) in length-\(n\) factors. Precisely the following integer pairs occur:
\[
(j,c):\quad p_n\le j\le q_n,\qquad
c\in\begin{cases}
\{0\},&n-j\text{ even},\\
\{-1,1\},&n-j\text{ odd},
\end{cases}
\]
where \(j=|u|_1\) and \(c=|u|_0-|u|_2\). All such pairs correspond to genuine factors, not merely solutions of necessary inequalities. The same source establishes
\[
p_1=0,\quad q_1=1,\qquad
p_{4n-1}=n+p_n-1,\quad q_{4n-1}=n+q_n.
\]
The present finding does not reprove that published infinite-word spectrum; it deduces a new integer-valuation classification and a quantitative divergence statement from it.

## Proof

**1. Unbounded consecutive count spectrum.** Define \(n_0=1\) and \(n_{k+1}=4n_k-1\), giving the explicit \(n_k\) above. By the cited recurrences,
\[
q_{n_{k+1}}-p_{n_{k+1}}=(q_{n_k}-p_{n_k})+1.
\]
As \(q_1-p_1=1\), it follows that
\[
q_{n_k}-p_{n_k}=k+1.\tag{1}
\]
Thus the allowed interval of \(1\)-counts contains \(k+2\) consecutive integers.

**2. Exact arithmetic of two Parikh vectors.** For an occurring pair \((j,c)\), its multiplicities of \(0\) and \(2\) are
\[
|u|_0=\frac{n-j+c}{2},\qquad
|u|_2=\frac{n-j-c}{2}.
\]
The associated valuation sum is therefore
\[
S_n(j,c)=\frac{(a_0+a_2)n-Aj+Ec}{2}.\tag{2}
\]
For two occurring pairs \((j,c)\) and \((j',c')\), equality of sums is equivalent to
\[
A(j-j')=E(c-c').\tag{3}
\]
Also \(j\equiv n-c\pmod2\), so \(j-j'\equiv c-c'\pmod2\). Only \(c-c'\in\{-2,-1,0,1,2\}\) is possible.

**3. Sufficiency.** Assume \(A\ne0\) and \(A\nmid E\). If \(c=c'\), Equation (3) forces \(j=j'\). If \(|c-c'|=1\), Equation (3) would imply \(A\mid E\), contrary to hypothesis. If \(|c-c'|=2\), parity forces \(j-j'\) to be even, and dividing Equation (3) by \(2\) again gives \(A\mid E\). Thus no two distinct occurring Parikh vectors have equal sums at any length. The two complexities coincide for every \(n\ge1\).

**4. Necessity and divergence when \(A=0\).** In Equation (2), the sum depends only on \(n\) and \(c\). Since \(c\) has at most three values, \(\rho_{\mathbf a}(n)\le3\) for every \(n\), even when \(E\ne0\); if \(E=0\), it is exactly \(1\). Each permitted \(j\) at length \(n_k\) gives at least one different Parikh vector, so Equation (1) gives \(\rho_{\rm ab}(n_k)\ge k+2\). The deficit is therefore at least \(k-1\) and diverges.

**5. Necessity and divergence when \(A\ne0\) and \(A\mid E\).** Put \(h=E/A\in\mathbb Z\). For every integer \(j\) satisfying
\[
p_{n_k}\le j\le q_{n_k},\qquad
p_{n_k}\le j-2h\le q_{n_k},\qquad
n_k-j\text{ odd},
\]
both \((j,1)\) and \((j-2h,-1)\) belong to the actual Parikh spectrum, by its exact description. Equation (3) holds because \(j-(j-2h)=2h\) and \(1-(-1)=2\). These are *distinct* Parikh vectors with equal sums (also when \(h=0\), since the two values of \(c\) differ).

Write \(W=q_{n_k}-p_{n_k}=k+1\). The set of eligible \(j\) is an interval of \(\max\{0,W-2|h|+1\}\) integers, restricted to one parity. Therefore there are at least
\[
\max\left\{0,\left\lfloor\frac{k+2-2|h|}{2}\right\rfloor\right\}
\]
choices. The associated collision pairs are vertex-disjoint: first members all have \(c=1\), second members all have \(c=-1\), and both maps from \(j\) are injective. Identifying each of these disjoint pairs under the weight-sum equivalence reduces the number of classes by at least the number of pairs. This proves the quantitative deficit bound and its divergence with \(k\).

The cases in Steps 3--5 exhaust all integer valuations, proving the equivalence and the claimed dichotomy. \(\square\)

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The checker constructs a 393216-symbol prefix directly by iterating the morphism, enumerates the Parikh vectors of its length-\(n\) windows for fourteen specified lengths through \(171\), checks the parity-resolved spectrum in those finite samples, and compares weighted sums for twelve explicitly selected integer valuations. It reproduces the earlier reported first failures at lengths \(11\) for weights \((0,1,3)\) and \(43\) for weights \((0,1,4)\), and verifies the initial five lengths \(n_k\) and their widths. It separately tests 343 small integer valuations on a *synthetic* 61-position parity spectrum of width 20; this tests the arithmetic equivalence, not infinite-word occurrence. For valuations whose first collision may occur beyond the finite-word samples, the checker does **not** mistake a finite absence for infinite injectivity.

The infinite assertions in the theorem follow from the cited rigorous Parikh-spectrum and recurrence theorems together with Steps 1--5, not from the finite checks.

## Relationship to prior work

Popoli, Shallit and Stipulanti (2024), Question 30 and Theorem 31, motivated preservation of abelian complexity under valuation. Their result proves equality for the particular one-parameter relabeling \((0,1,\lambda)\) when \(\lambda\ge5\), and reports the first failures for \(\lambda=3,4\). Substitution into the present criterion gives \(A=\lambda-2\) and \(E=-\lambda\); among integers \(\lambda\ge2\), the condition holds exactly when \(\lambda\ge5\). The earlier one-parameter theorem is thus recovered and extended to an explicit necessary-and-sufficient condition for *all* integer triples. The divergent-gap part is also not asserted there.

Blanchet-Sadri, Currie, Rampersad and Fox (2014) already proved the precise Parikh-vector spectrum and extremal-count recurrences used in this proof. Those strong structural inputs are prior results, and the arithmetic classification is a consequence of them; their paper does not itself address the classification of all integer valuations or the weighted-complexity gap. Machacek (2025) later investigated permutation-group orbit complexity of the same ternary word, a different equivalence relation. Chen, Wen and Wu (2018/2019) studied additive complexity of the distinct substitution \(0\mapsto01,1\mapsto12,2\mapsto20\), not this ternary Thue word.

## Limitations

The result concerns the single specified fixed point and its integer-valued one-dimensional letter sums; no claim is made for arbitrary ternary words, real-valued weights, or multidimensional valuations. The lower bounds describe a sparse explicit sequence of lengths, not all lengths, and are not asserted optimal. The complete infinite-word Parikh-spectrum facts are used from their published proof, while `verify.py` is only a finite sanity check. Priority beyond the cited and inspected sources cannot be guaranteed; an independently developed or unindexed equivalent criterion might exist.

## References

1. P. Popoli, J. Shallit and M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (first public 2024-10-03), Section 4, Question 30 and Theorem 31. https://arxiv.org/html/2410.02409v1
2. F. Blanchet-Sadri, J. D. Currie, N. Rampersad and N. Fox, *Abelian Complexity of Fixed Point of Morphism 0→012, 1→02, 2→1*, Integers 14 (2014), A11, Lemma 8 and Theorem 2. https://math.colgate.edu/~integers/o11/o11.pdf
3. J. Machacek, *Group Actions and Some Combinatorics on Words with vtm*, arXiv:2509.26613v1 (2025), Section 5. https://arxiv.org/html/2509.26613v1
4. J. Chen, Z. Wen and W. Wu, *On the additive complexity of a Thue-Morse-like sequence*, arXiv:1802.03610 (2018), later Discrete Applied Mathematics 260 (2019), 98–108. https://arxiv.org/abs/1802.03610
