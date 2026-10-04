# Exact two-crossing transport law for Bernoulli pair balancing

## Finding

Let \(A\) be a Poisson-binomial random variable, independent of two selected
Bernoulli trials. Compare
\[
W=A+B_p+B_q
\]
with
\[
\widetilde W=A+B_{\widetilde p}+B_{\widetilde q},
\]
where
\[
p+q=\widetilde p+\widetilde q
\]
and
\[
\delta=\widetilde p\widetilde q-pq\ge0.
\]
Thus the second pair is at least as balanced as the first.

Write
\[
a_k=\Pr(A=k),
\]
and extend \(a_k\) by zero outside the support. Define the backward differences
\[
\Delta a_k=a_k-a_{k-1}
\]
and
\[
\Delta^2a_k=a_k-2a_{k-1}+a_{k-2}.
\]

Then the entire distributional change is
\[
\boxed{
\Pr(\widetilde W=k)-\Pr(W=k)
=
\delta\,\Delta^2a_k.
}
\tag{1}
\]

The nonzero terms of \((\Delta^2a_k)\) have exactly two sign changes and hence
the sign pattern
\[
+,\,-,\,+.
\tag{2}
\]
Consequently, pair balancing removes probability from one consecutive central
band and adds probability in both tails.

The cumulative distribution functions satisfy the sharper first-difference
identity
\[
\boxed{
F_{\widetilde W}(k)-F_W(k)
=
\delta\,\Delta a_k.
}
\tag{3}
\]
Since every Poisson-binomial mass function is unimodal, the right side changes
sign at most once: the two CDFs cross only across the modal plateau of the
background law.

Several probability metrics therefore have exact closed forms:
\[
\boxed{
d_{\rm TV}(\widetilde W,W)
=
\frac{\delta}{2}\sum_k|\Delta^2a_k|,
}
\tag{4}
\]
\[
\boxed{
d_K(\widetilde W,W)
=
\delta\max_k|\Delta a_k|,
}
\tag{5}
\]
and
\[
\boxed{
W_1(\widetilde W,W)
=
2\delta\max_k a_k.
}
\tag{6}
\]
Here \(W_1\) is the ordinary Wasserstein distance for cost \(|x-y|\).

The stop-loss transform is even more local. For every integer threshold \(h\),
\[
\boxed{
\mathbb E(\widetilde W-h)_+
-
\mathbb E(W-h)_+
=
\delta\,a_{h-1}.
}
\tag{7}
\]

More generally, for every function \(\phi\) for which the expectations exist,
\[
\mathbb E\phi(\widetilde W)-\mathbb E\phi(W)
=
\delta\,
\mathbb E\!\left[
\phi(A+2)-2\phi(A+1)+\phi(A)
\right].
\tag{8}
\]
Thus balancing increases the expectation of every convex \(\phi\), recovering
the classical convex-order direction, while (1)--(7) quantify the entire
single-step redistribution.

## Assumptions and scope

The background \(A\) is a finite sum of independent Bernoulli variables.
Parameters equal to zero or one are allowed. The empty sum is also allowed.

The pair sum is held fixed. The condition \(\delta\ge0\) is exactly the
condition that the replacement pair is at least as balanced: for a fixed sum,
the product is maximized when the two probabilities are equal.

The exact algebraic identities (1), (3), (4), (5), (7), and (8) hold for any
finite-support integer-valued background. The two-crossing statement (2) and
the modal simplification (6) use the Poisson-binomial structure.

## Proof

Let
\[
s=p+q=\widetilde p+\widetilde q
\]
and
\[
r=pq.
\]
The law of \(B_p+B_q\) has masses
\[
1-s+r,\qquad s-2r,\qquad r
\]
at \(0,1,2\). Replacing \(r\) by \(r+\delta\) therefore changes these three
masses by
\[
\delta,\qquad -2\delta,\qquad \delta.
\]
Convolving with the background mass function immediately gives (1).

Summing (1) over all indices at most \(k\) telescopes:
\[
\sum_{j\le k}\Delta^2a_j
=
\Delta a_k.
\]
This proves (3).

We next prove the two-crossing structure. The probability generating
polynomial of \(A\) is
\[
P(z)=\prod_i(1-\alpha_i+\alpha_i z),
\]
where the \(\alpha_i\) are the Bernoulli parameters. After deterministic
successes are factored out as a power of \(z\), every nonzero root of \(P\) is
real and nonpositive. The generating polynomial of the signed sequence
\((\Delta^2a_k)\) is
\[
(z-1)^2P(z).
\tag{9}
\]
It therefore has exactly two positive roots, counted with multiplicity, and
all remaining nonzero roots are negative.

We use the following elementary real-rooted form of Descartes' rule: if a
real polynomial has only real nonzero roots, then the number of sign changes
in its coefficient sequence, after zero coefficients are removed, equals the
number of positive roots counted with multiplicity. One proof applies
Descartes' rule to the polynomial and to its reflection \(z\mapsto -z\);
when no coefficient vanishes, the two coefficient variation counts add to the
degree, so both Descartes inequalities are equalities. Vanishing coefficients
follow by an arbitrarily small root perturbation preserving root signs.

Applying this lemma to (9) gives exactly two sign changes. The first and last
nonzero coefficients are positive, so the pattern is \(+,-,+\), proving (2).

The same real-rooted generating polynomial also gives log-concavity of the
Poisson-binomial coefficient sequence by Newton's inequalities. Hence
\((a_k)\) is unimodal. Its first differences are nonnegative up to a modal
plateau and nonpositive thereafter. Identity (3) therefore gives the asserted
single CDF crossing.

Equation (4) is the definition of total variation applied to (1), and (5)
follows from (3). For integrable integer-valued laws,
\[
W_1(X,Y)=\sum_{k\in\mathbb Z}|F_X(k)-F_Y(k)|.
\]
Using (3),
\[
W_1(\widetilde W,W)
=
\delta\sum_k|\Delta a_k|.
\]
For any finite unimodal probability mass function that begins and ends at
zero, the total variation of the sequence is twice its maximum:
\[
\sum_k|\Delta a_k|=2\max_k a_k.
\]
This proves (6).

For (8), condition on \(A\) and use the three signed changes
\[
\delta,\,-2\delta,\,\delta.
\]
Taking
\[
\phi(x)=(x-h)_+
\]
gives
\[
\phi(x+2)-2\phi(x+1)+\phi(x)
=
\mathbf 1_{\{x=h-1\}},
\]
which proves (7).

## Verification

The accompanying exact-rational checker constructs thousands of
Poisson-binomial backgrounds with rational Bernoulli parameters. It verifies
the signed convolution identity, the telescoping CDF identity, all three
metric formulas, and the stop-loss formula exactly.

For every tested background it also removes zero coefficients from
\((\Delta^2a_k)\) and checks exactly two sign changes with the pattern
\(+,-,+\). The checker verifies unimodality and the equality
\[
\sum_k|\Delta a_k|=2\max_k a_k.
\]

The computation is supplementary. The universal proof is the generating
polynomial and finite-difference argument above.

## Relationship to prior work

Hoeffding's classical work on the number of successes in independent trials
optimizes expectations of arbitrary functions under a fixed mean and proves
that balancing increases expectations of convex functions. His algebra
contains the finite-difference mechanism behind pair transfers. Accordingly,
the convex-order direction in (8) is not claimed as new. The inspected text
does not state the two-crossing probability-mass structure, the one-crossing
CDF identity as a distributional comparison, or the exact total-variation,
Kolmogorov, and Wasserstein formulas (4)--(6).

Wang gives a combinatorial treatment of Poisson-binomial laws and proves the
strong unimodality inequality needed to control the first-difference signs.
The inspected paper also compares homogeneous and heterogeneous Bernoulli
sums, but it does not analyze a single fixed-sum pair transfer or derive its
exact transport cost.

Roos develops Krawtchouk expansions for binomial approximation of
Poisson-binomial laws. The second finite difference of a binomial mass
function appears explicitly in the leading total-variation approximation
term. That comparison is between a heterogeneous sum and a binomial proxy,
not between two exact Poisson-binomial laws differing in one pair, and the
inspected paper does not give (1)--(7).

Yu's relative-log-concavity framework places binomial and Poisson-binomial
laws in convex-order context, while Sason studies total-variation bounds for
Poisson-binomial approximation. Neither inspected line of work states the
exact two-crossing pair-transfer law or the modal-mass coefficient in (6).

Targeted semantic searches for Bernoulli pair transfers, probability-mass
crossings, total variation, Wasserstein distance, and fixed-sum majorization
did not locate the combined statement.

## Limitations

The \(+,-,+\) mass-difference pattern uses the real-rooted generating
polynomial of a Poisson-binomial background. An arbitrary integer-valued
background still satisfies the finite-difference identities but need not have
two mass crossings.

The result treats a single balancing step. Distances along a sequence of
several balancing steps do not generally add, because the background and its
modal mass change after each step.

The originality search was targeted. Total-positivity or older convolution
literature may contain an equivalent two-crossing formulation under different
terminology.

## References

1. W. Hoeffding, “On the Distribution of the Number of Successes in
   Independent Trials,” Institute of Statistics Mimeograph Series No. 128,
   1955; later *Annals of Mathematical Statistics* 27 (1956), 713–721.
2. Y. H. Wang, “On the Number of Successes in Independent Trials,”
   *Statistica Sinica* 3 (1993), 295–312.
3. B. Roos, “Binomial Approximation to the Poisson Binomial Distribution:
   The Krawtchouk Expansion,” *Theory of Probability and Its Applications*
   45, 258–272.
4. Y. Yu, “Relative log-concavity and a pair of triangle inequalities,”
   arXiv:1010.2043, first submitted 2010-10-11.
5. I. Sason, “On the Entropy of Sums of Bernoulli Random Variables via the
   Chen-Stein Method,” arXiv:1301.7504, first submitted 2013-01-31.
