# A parity phase diagram for conditional one-step counting-modal proportions

## Finding

Fix integers \(k\geq1\), \(1\leq a<2^k\), and \(h\geq1\). Let \(\chi\) be a propositional formula holding for exactly \(a\) of the \(2^k\) Boolean assignments to \(k\) atoms. Set \(p=a/2^k\) and \(\rho=p/(1-p)\). Consider the fixed depth-one formulas of counting modal logic
\[
\Psi_0 := (\#\chi\geq\#\neg\chi),\qquad
\Phi_h := (\#\chi-\#\neg\chi\geq h).
\]
On a uniformly and independently Boolean-labelled complete rooted \(n\)-ary tree of height one, let \(C_n(h)\) be the proportion of \(\Psi_0\)-satisfying labelled trees also satisfying \(\Phi_h\). Then, if \(0<p<1/2\),
\[
\boxed{\lim_{m\to\infty}C_{2m}(h)=\rho^{\lceil h/2\rceil},\qquad
\lim_{m\to\infty}C_{2m+1}(h)=\rho^{\lceil(h-1)/2\rceil}.}
\]
If \(1/2\leq p<1\), the full sequence \(C_n(h)\) tends to \(1\). Thus, in the rare-event phase \(p<1/2\), the conditional proportion converges **exactly when \(h\) is even**; with an odd positive threshold it has two distinct parity limits. In particular, for \(\chi=p_1\wedge p_2\) and \(h=3\), the two limits are \(1/9\) along even branching degrees and \(1/3\) along odd degrees.

There is also a complete conditional excess law: for \(p<1/2\), let \(X_n\) count \(\chi\)-satisfying children and let \(J_n=X_n-\lceil n/2\rceil\). Conditionally on \(\Psi_0\), the distribution of \(J_n\) converges in total variation, without passing to parity subsequences, to the geometric distribution \(\Pr(J=j)=(1-\rho)\rho^j\) on nonnegative integers.

## Assumptions and scope

The language has counting terms \(\#\varphi\) equal to the number of immediate successors satisfying \(\varphi\), Boolean negation and integer comparisons. The rooted tree has one root and exactly \(n\geq1\) distinguished children, with no further successors. Each world's \(k\) propositional atoms are sampled independently and uniformly. All \(2^{k(n+1)}\) labelled valuations are equiprobable. The root valuation does not influence either formula, so the relative number of models is the corresponding probability for \(n\) independent leaves. The same formulas are used for every \(n\); only the branching degree changes. The denominator is positive for every \(n\) since \(p>0\).

The theorem is not asserted for nonuniform child labels, dependent labels, arbitrary finite directed graphs, random unlabelled trees, formulas with growing thresholds, or arbitrary conditional modal formulas.

## Proof

Let \(X_n\) denote the number of \(\chi\)-satisfying children. Since \(\chi\) holds for \(a\) of the \(2^k\) equally likely atomic types, \(X_n\sim\operatorname{Bin}(n,p)\). The truth conditions are
\[
\Psi_0\iff X_n\geq \lceil n/2\rceil,
\qquad \Phi_h\iff 2X_n-n\geq h.
\]
Set \(b_n=\lceil n/2\rceil\) and \(w_n(j)=\Pr(X_n=b_n+j)/\Pr(X_n=b_n)\) for \(0\leq j\leq n-b_n\), and \(w_n(j)=0\) beyond that range. Binomial coefficients give the **exact** ratio
\[
w_n(j)=\rho^j\prod_{\ell=1}^{j}
\frac{n-b_n-\ell+1}{b_n+\ell}.
\]
For \(0<p<1/2\), each factor in the product is at most one, so \(0\leq w_n(j)\leq\rho^j\); for every fixed \(j\), all factors tend to one. Dominated convergence for countable sums yields
\[
\sum_{j\geq0}w_n(j)\longrightarrow\frac1{1-\rho},
\qquad
\Pr(J_n=j\mid\Psi_0)
=\frac{w_n(j)}{\sum_{t\geq0}w_n(t)}
\longrightarrow(1-\rho)\rho^j.
\]
Because the distributions are probability measures on a countable set and have pointwise limits summing to one, the convergence is in total variation (equivalently, combine domination with the normalization limit). The parity identity
\[
2X_n-n=2J_n+(n\bmod 2)
\]
shows that \(\Phi_h\) under \(\Psi_0\) is precisely the event \(J_n\geq\lceil(h-(n\bmod 2))/2\rceil\). The geometric tail \(\Pr(J\geq t)=\rho^t\) for integers \(t\geq0\) gives the displayed limits. If \(h\) is even, the two ceilings coincide. If \(h\) is odd, they differ by one, and since \(0<\rho<1\), the limits differ.

For \(p<1/2\), the probability of the conditioning event itself tends to zero exponentially: the Chernoff bound gives \(\Pr(\Psi_0)\leq\exp[-nD(1/2\|p)]\), with \(D(1/2\|p)=\tfrac12\log(1/[4p(1-p)])>0\). Consequently both unconditioned formula proportions vanish even though their ratio can have two distinct positive subsequential limits.

At \(p=1/2\), symmetry gives \(\Pr(\Psi_0)\geq1/2\). Only at most \(\lceil h/2\rceil\) binomial masses near the center are in \(\Psi_0\setminus\Phi_h\), and each such mass is \(O(n^{-1/2})\) by the central-binomial bound. Hence \(1-C_n(h)=O(n^{-1/2})\). For \(p>1/2\), the law of large numbers gives \(\Pr(\Phi_h)\to1\), and therefore \(\Pr(\Psi_0)\to1\); as \(\Phi_h\Rightarrow\Psi_0\), it follows that \(C_n(h)\to1\). This proves all cases and all claims.

## Verification

The supplied standalone `checker.py` runs with Python 3 and no third-party dependencies (`python3 checker.py`). It independently enumerates all \(4^n\) leaf-colourings for \(1\leq n\leq7\) in the concrete case \(p=1/4\), compares them with exact rational binomial probabilities, and cross-checks stable tail-ratio summation against exact rational evaluation for \(n\leq27\), four Bernoulli parameters and thresholds \(1\leq h\leq6\). Larger numerical checks inspect the predicted two parity limits for several thresholds. The checker returns `ALL_CHECKS_OK`. This numerical evidence is supplementary: the general theorem is established by the binomial-ratio and convergence arguments above, not by exhaustive finite experiments.

## Relationship to prior work

Ghosh and Schwarzentruber study counting-modal logic, uniform finite-tree model proportions and limits; their section on further questions explicitly asks for conditional proportions of one formula among models satisfying another. Their established unconditional limit/nonconvergence framework does not, in the sections inspected, supply this sharp conditional one-step parity classification or geometric excess law. Classical binomial tail-ratio/large-deviation techniques underlie the proof and are **not** claimed to be new. The contribution is a directly expressible fixed-formula counterexample and the complete conditional phase boundary in the specified random-modal model. Unconditional residue-class constructions involving deeper modal formulas concern a distinct limiting problem and by themselves do not determine these conditional probabilities.

## Limitations

Historical priority is not independently certified; an older theorem on geometric excess laws for binomial tails could immediately yield the probabilistic portion through this modal translation. The conditional model proportion is deliberately restricted to a fixed pair of natural depth-one threshold formulas and independent uniform Boolean labels. No general algorithm for arbitrary conditional counting-modal formulas is claimed. A separate independent scientific audit has not been performed.

## References

1. Avijeet Ghosh and François Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187, first publicly submitted 19 October 2026, https://arxiv.org/abs/2610.26187 .
2. Standard binomial mass-ratio identity and central-binomial bounds; both are explicitly derived or invoked in the proof. No historical-priority claim is made for the underlying tail asymptotics.
