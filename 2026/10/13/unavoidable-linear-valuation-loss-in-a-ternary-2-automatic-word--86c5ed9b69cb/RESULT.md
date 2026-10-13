# Unavoidable linear valuation loss in a ternary \(2\)-automatic word

## Finding

Let \(\mathbf w=(w_j)_{j\geq0}\) be the ternary infinite word
\[
w_0=0,\qquad w_j=\bigl(\lfloor\log_2 j\rfloor\bmod 3\bigr)\quad(j\geq1).
\]
For any integer valuation \(v:\{0,1,2\}\to\mathbb Z\), let \(\rho_v(n)\) count distinct sums of the valuations of the letters in length-\(n\) contiguous factors, and let \(\rho_{\mathrm{ab}}(n)\) count the distinct Parikh vectors of such factors. The following is one theorem about this word.

**Theorem (unavoidable valuation loss).** The word \(\mathbf w\) is aperiodic and \(2\)-automatic; its ordinary factor complexity \(P(n)\) satisfies \(P(n)\leq5n+2\), while \(\rho_{\mathrm{ab}}(n)\geq3n\) for every \(n\geq1\). If the three values of \(v\) are distinct, order the letters \(a,b,c\) so that \(v(a)<v(b)<v(c)\), and put
\[
\alpha=v(b)-v(a),\qquad \beta=v(c)-v(a),\qquad g=\gcd(\alpha,\beta).
\]
For every positive integer \(n\),
\[
\boxed{\rho_{\mathrm{ab}}(n)-\rho_v(n)\ \geq\ \left\lfloor\frac{ng}{\beta}\right\rfloor.}
\]
If \(v\) is not injective, its additive complexity already differs from the abelian complexity at \(n=1\). Thus no integer valuation preserves the abelian complexity at every length, and every injective valuation incurs a positive linear asymptotic loss. For the natural valuation \(v(i)=i\), the additive complexity is **exactly**
\[
\boxed{\rho_v(n)=2n+1\quad(n\geq1)}.
\]
Three is the least alphabet size admitting any sequence with this universal obstruction: on every alphabet of at most two letters, an injective integer valuation reproduces abelian complexity for every word.

## Assumptions and scope

The sequence is one-sided, indexed from zero. A *factor* of length \(n\) starts at any nonnegative index and contains the next \(n\) letters. Parikh vectors record symbol multiplicities in the fixed order \(0,1,2\). Distinct additive sums, not their multiplicities, are counted in \(\rho_v(n)\). The valuation is fixed across all lengths and has **integer** values; negative integers and repeated values are permitted. No statement is made for arbitrary real or irrational weights.

The powers-of-two blocks are explicit: for each \(k\geq0\), the positions \(2^k,\ldots,2^{k+1}-1\) form a constant run of length \(2^k\) with letter \(k\bmod3\). The initial letter at position zero is an additional \(0\).

## Proof

**1. Triangle-edge factor lemma.** Fix distinct letters \(a,b\in\{0,1,2\}\), a length \(n\geq1\), and \(0\leq j\leq n\). The cyclic sequence of run letters is \(0,1,2,0,1,2,\ldots\), so it contains the ordered adjacency \(a,b\) or \(b,a\) infinitely often. Both adjacent run lengths tend to infinity. Choose an occurrence for which each run has length at least \(n\). A window straddling that boundary realizes a factor with exactly \(n-j\) copies of \(a\) and \(j\) copies of \(b\), irrespective of which letter occurs first. This holds for all three unordered pairs and every \(j\). The corresponding lattice points form the three edges of a triangular Parikh lattice and have \(3(n+1)-3=3n\) distinct elements. Thus \(\rho_{\mathrm{ab}}(n)\geq3n\).

**2. Uniform linear factor bound.** Choose the least nonnegative \(K\) with \(2^K\geq n\). There are only \(2^K<2n\) factor starting positions before position \(2^K\). Every run starting at or after position \(2^K\) has length at least \(n\), so every length-\(n\) factor beginning there contains at most one change of letter and is one of at most \(3(n+1)\) two-run words, corresponding to the three cyclic ordered adjacencies. Therefore \(P(n)\leq2^K+3(n+1)\leq5n+2\). In particular the obstruction below is not the quadratic-counting obstruction of a word containing every ternary factor.

**3. Exact natural additive complexity.** The valuation \(v(i)=i\) assigns every length-\(n\) factor an integer sum between \(0\) and \(2n\). Across a long \(0,1\) run boundary all sums \(0,1,\ldots,n\) occur; across a long \(1,2\) boundary all sums \(n,n+1,\ldots,2n\) occur. Thus all \(2n+1\) sums occur and no other sum is possible. This proves the exact formula.

**4. All injective integer valuations.** Fix \(v\) with distinct values, order \(a,b,c\) by their weights, and define \(\alpha,\beta,g\) as in the theorem. For each integer
\[
1\leq t\leq\left\lfloor\frac{ng}{\beta}\right\rfloor,
\]
set \(j=t\beta/g\) and \(i=t\alpha/g\). Then \(1\leq i<j\leq n\). By Step 1 there is a length-\(n\) factor with Parikh vector of \(a^{n-j}b^j\), and another with the Parikh vector of \(a^{n-i}c^i\). Their Parikh vectors are different, but both have valuation sum
\[
 n\,v(a)+j\alpha=n\,v(a)+i\beta
 =n\,v(a)+\frac{t\alpha\beta}{g}.
\]
As \(t\) varies, these common sums are distinct. Hence there are at least \(\lfloor ng/\beta\rfloor\) different, pairwise disjoint collisions in the map from occurring Parikh vectors to additive sums. Each collision lowers the cardinality of its image by at least one. This yields the displayed deficit for every \(n\geq1\) and a positive slope \(g/\beta\) for each fixed injective \(v\).

**5. Repeated values, automaticity, and optimal alphabet.** If two letters receive the same value, the three distinct length-one Parikh vectors map to at most two sums, giving \(\rho_{\mathrm{ab}}(1)>\rho_v(1)\). For automaticity, use a four-state deterministic automaton with output reading the usual binary expansion most-significant digit first: an initial state outputs \(0\), ignores leading zeroes, and on its first \(1\) enters state \(q_0\); from \(q_r\), either input digit goes to \(q_{(r+1)\bmod3}\), with output \(r\) at \(q_r\). It computes the bit length minus one modulo three and handles the input zero. The unbounded runs of each of three symbols rule out ultimate periodicity. Finally, on a one- or two-letter alphabet, assigning weights \(0,1\) to the distinct letters makes the sum of a length-\(n\) factor determine its Parikh vector, proving alphabet minimality. This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 and the standard library. The checker tests the four-state automaton against the direct definition for the first 65,536 positions; exhaustively enumerates distinct factors and Parikh vectors in a prefix of length 8,192 for factor lengths \(1\) through \(48\); verifies all three Parikh-lattice edges, the exact natural sum spectrum, and the factor bound; and checks the all-valuation inequality for all 343 weight assignments in \(\{-3,-2,\ldots,3\}^3\). The checks are independent finite corroboration. The proof above, not the finite cutoff, establishes the assertions for all positions, lengths, and integer valuations.

## Relationship to prior work

Popoli, Shallit, and Stipulanti introduce additive complexity, formulate the valuation-existence question (Question 31), and prove positive preservation results under balance or particular morphic structure (Theorems 32 and 33). The present theorem supplies a complementary **automatic, linear-factor-complexity** obstruction for every integer valuation. A full-language word would have a much easier quadratic-versus-linear pigeonhole obstruction; here ordinary factor complexity is already linear, and the proof instead uses a forced collision on a triangular family of Parikh vectors. The general abelian-complexity automatic-sequence results of Shallit concern different hypotheses and do not imply this obstruction. The result does not claim to settle valuation questions for uniformly recurrent or balanced sequences.

## Limitations

The example is not uniformly recurrent. The quantitative slope depends on the particular integer valuation, so there is no asserted positive lower bound uniform over valuations. The exact full abelian-complexity function of this word is not determined; only its linear lower and upper bounds are used. No result for arbitrary real-valued valuations or arbitrary automatic words is claimed. The originality comparison is confined to the inspected literature and indexed public findings; unpublished or unindexed equivalent statements remain possible.

## References

1. P. Popoli, J. Shallit, and M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (first posted 2024-10-03), especially Sections 3 and 5, Question 31, and Theorems 32–33. https://arxiv.org/abs/2410.02409
2. J. Shallit, *Abelian Complexity and Synchronization*, arXiv:2011.00453v3 (2020), especially Section 2 and Theorem 1. https://arxiv.org/abs/2011.00453
