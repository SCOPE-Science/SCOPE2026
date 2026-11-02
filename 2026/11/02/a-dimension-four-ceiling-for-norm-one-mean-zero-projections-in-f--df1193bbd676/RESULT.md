# A dimension-four ceiling for norm-one mean-zero projections in finite Lorentz spaces

## Finding

Let \(n\ge 2\), and let \(w_1\ge\cdots\ge w_n\ge0\) be real weights with \(w_1>0\). On real \(\mathbb R^n\) put
\[
N_w(x)=\sum_{j=1}^n w_j|x|_{(j)},
\]
where \(|x|_{(1)}\ge\cdots\ge |x|_{(n)}\) are the decreasing rearranged absolute coordinates. Write \(H=\{x:\sum_i x_i=0\}\).

**Theorem.** The subspace \(H\) admits a norm-one linear projection in \((\mathbb R^n,N_w)\) exactly in the following cases:

1. \(n=2\): arbitrary permitted weights;
2. \(n=3\): \(w_1=w_2+w_3\);
3. \(n=4\): \(w_1=w_2+w_3\) and \(w_4=0\).

For **every** \(n\ge5\) and every permitted nonzero nonincreasing weight profile, the optimal projection norm is strictly greater than one. In particular, if every weight is strictly positive, dimension three is the largest nontrivial dimension allowing a norm-one projection.

There is also an exact finite formula for the optimal projection norm. Define \(W_k=\sum_{j=1}^k w_j\). For \(1\le k\le n\) and \(\lceil k/2\rceil\le a\le k\), put \(m=(2a-k)/n\) and let \(\rho_1\ge\cdots\ge\rho_n\) be the rearrangement of the multiset containing \(a\) copies of \(1-m\), \(k-a\) copies of \(1+m\), and \(n-k\) copies of \(m\). Then
\[
\boxed{\lambda(H,N_w)=\max_{1\le k\le n}\ \max_{\lceil k/2\rceil\le a\le k}\frac{\sum_{j=1}^n w_j\rho_j}{W_k}.}
\]
Here \(\lambda\) is the infimum of operator norms among linear projections onto \(H\). Every denominator is positive, so the formula is valid even with zero tail weights.

## Assumptions and scope

The scalars are real. The dimension is finite, and the norm uses decreasing nonnegative weights, not arbitrary signed weights. No strict positivity of tail weights is assumed. The theorem concerns linear projections onto the codimension-one coordinate-sum-zero hyperplane, not nonlinear nearest-point maps, arbitrary hyperplanes, or other Lorentz parameters. The exact formula covers all allowed weights and every \(n\ge2\); the norm-one classification is a special consequence.

## Proof

**1. The symmetric projection is optimal.** Write \(\sigma(x)=\sum_i x_i\). Every linear projection \(Q\) onto \(H=\ker\sigma\) has the form \(Qx=x-\sigma(x)v\) for a vector \(v\) satisfying \(\sigma(v)=1\). The permutations of coordinates act isometrically on \(N_w\) and preserve \(H\). Average the conjugate projections \(U_\pi^{-1}QU_\pi\) over all permutations. The resulting projection is
\[
Px=x-\frac{\sigma(x)}n\mathbf1,
\]
and its norm is at most \(\|Q\|\), by convexity of the operator norm. Therefore \(\lambda(H,N_w)=\|P\|\).

**2. Exact operator norm.** Given any \(x\), list its absolute coordinate values in nonincreasing order \(c_1\ge\cdots\ge c_n\), set \(c_{n+1}=0\), and write the signed top-\(k\) indicator as \(u_k\). The layer-cake decomposition
\[
x=\sum_{k=1}^n(c_k-c_{k+1})u_k,
\qquad
N_w(x)=\sum_{k=1}^n(c_k-c_{k+1})W_k
\]
holds even for repeated magnitudes and zeros. Thus \(\|Px\|\le\bigl(\max_{k,u_k}\|Pu_k\|/W_k\bigr)N_w(x)\), with equality possible for an indicator. By permutations and global sign reversal, an indicator with exactly \(k\) nonzero coordinates has \(a\ge k-a\) entries equal to \(+1\), the rest equal to \(-1\). Its mean is \(m=(2a-k)/n\), and its centered absolute coordinates are precisely the multiset in the statement. This proves the exact finite maximum formula.

**3. Reduction to generic centered vectors.** Every \(x\) has a unique representation \(x=y+t\mathbf1\) with \(y\in H\) and \(t=\sigma(x)/n\). Hence \(\|P\|=1\) if and only if
\[
N_w(y)\le N_w(y+t\mathbf1)\quad\text{for every }y\in H,\ t\in\mathbb R.
\]
The function of \(t\) is convex. Call \(y\) generic if all its coordinates are nonzero and their absolute values are pairwise distinct. For a generic \(y\in H\), order its coordinates so that \(|y_1|>\cdots>|y_n|>0\) and define \(\varepsilon_i=\operatorname{sgn}(y_i)\). The derivative of \(t\mapsto N_w(y+t\mathbf1)\) at zero is exactly \(\sum_{i=1}^n w_i\varepsilon_i\). Thus norm-one projection is equivalent to this signed sum vanishing for every generic zero-sum vector. The reverse implication uses convexity for each generic \(y\) and then density and continuity to cover nongeneric \(y\). The generic vectors are dense in \(H\) because a finite number of proper hyperplanes \(y_i=0\) and \(y_i=\pm y_j\) cannot cover \(H\), for \(n\ge3\).

**4. Feasible sign sequences.** After reversing all signs, suppose \(\varepsilon_1=+1\). Put \(a_i=|y_i|\), so \(a_1>\cdots>a_n>0\), and define positive gaps \(d_j=a_j-a_{j+1}\), with \(a_{n+1}=0\). Let \(S_j=\sum_{i=1}^j\varepsilon_i\). Then
\[
\sum_i y_i=\sum_i\varepsilon_i a_i=\sum_{j=1}^n d_j S_j.
\]
Since \(S_1=1\), positive gaps can satisfy the zero-sum equality if and only if some prefix \(S_j<0\). Necessity is immediate. For sufficiency, first choose all gaps positive and arbitrarily small except two gaps with opposite-signed prefix coefficients, and adjust one of those two gaps to make the sum exactly zero; the resulting gaps remain strictly positive. This constructs the generic centered vector for **every** such sign sequence.

**5. Classification.** For \(n=3\), the only feasible sign sequence with first sign positive is \((+,-,-)\), forcing and being forced by \(w_1-w_2-w_3=0\). For \(n=4\), exactly \((+,-,-,-)\) and \((+,-,-,+)\) are feasible; their derivative conditions are \(w_1-w_2-w_3-w_4=0\) and \(w_1-w_2-w_3+w_4=0\). Both hold precisely when \(w_4=0\) and \(w_1=w_2+w_3\).

For every \(n\ge5\), all sign sequences starting \((+,-,-)\) and having arbitrary remaining signs are feasible. Comparing sequences that differ in a single later sign forces \(w_4=\cdots=w_n=0\) and \(w_1=w_2+w_3\). The additional feasible sign sequence \((+,+,-,-,-,+,\ldots,+)\) forces \(w_1+w_2-w_3=0\). Together these imply \(w_2=0\) and \(w_1=w_3\). Monotonicity then gives \(w_3=0\), contradicting \(w_1>0\). Therefore \(\|P\|>1\) for all \(n\ge5\).

For \(n=2\), the coordinate transposition \(S\) is an isometry, and \(P=(I-S)/2\), so \(\|P\|\le1\). Because \(P\) fixes nonzero vectors in \(H\), its norm is exactly one. The proof is complete.

## Verification

The accompanying standalone Python script `verify.py` uses rational arithmetic only. It checks the formula and norm-one classification on 780 nonincreasing weight profiles in dimensions two through seven, independently compares the indicator maximum against all ternary signed-support indicators through dimension five, and checks three boundary examples. It can be run with `python verify.py`. Its finite tests are diagnostic, not a substitute for the proof in the previous section.

Two explicit outcomes are \(\lambda=1\) for weights \((1,3/5,2/5)\) in dimension three and \((1,3/5,2/5,0)\) in dimension four. For dimension five with weights \((1,1/2,1/2,0,0)\), the exact formula gives \(\lambda=11/10>1\).

## Relationship to prior work

Existing Lorentz-space geometry and one-complementation literature studies extreme/smooth points and gives general conditions relating existence sets to norm-one projections. Ciesielski and Lewicki's 2018 work (§5, Theorem 5.2) proves that existence sets in a corresponding Lorentz sequence-space setting are one-complemented; this does not by itself classify the concrete zero-sum hyperplane for every finite nonincreasing weight vector. Their 2021 article develops general contractive/existence-set theory. The 2009 paper by Kamińska, Lee and Lewicki concerns precisely the \(d(w,1)\) family and is a materially relevant prior source, but only its abstract and surrounding accessible descriptions could be inspected; exact duplication risk therefore remains. The present claim is the explicit finite weight-by-dimension hyperplane classification and the signed-support optimal norm formula, not any general equivalence between existence sets and one-complementation.

## Limitations

This is a finite-dimensional real-space result. No generalization to other Lorentz exponents, complex scalars, infinite sequences or arbitrary hyperplanes is claimed. A complete comparison with the inaccessible 2009 full text remains unresolved bibliographically. Independent scientific audit and validation have not been performed.

## References

1. M. Ciesielski and G. Lewicki, *Sequence Lorentz spaces and their geometric structure*, arXiv:1805.06355, first public version 2018-05-16, §5. https://arxiv.org/abs/1805.06355
2. M. Ciesielski and G. Lewicki, *Some remarks on contractive and existence sets*, arXiv:2112.00366, first public version 2021-12-01. https://arxiv.org/abs/2112.00366
3. A. Kamińska, H. J. Lee and G. Lewicki, *Extreme and smooth points in Lorentz and Marcinkiewicz spaces with applications to contractive projections*, Rocky Mountain Journal of Mathematics 39 (2009), 1533–1572, DOI:10.1216/RMJ-2009-39-5-1533. (Abstract and available descriptions inspected, not the full paper.)
4. B. Randrianantoanina, *One-complemented subspaces of real sequence spaces*, arXiv:math/9702214, first version 1997-02-24 (a related different-exponent setting). https://arxiv.org/abs/math/9702214
