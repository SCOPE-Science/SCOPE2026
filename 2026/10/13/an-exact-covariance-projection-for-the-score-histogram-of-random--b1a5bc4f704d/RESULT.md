# An exact covariance projection for the score histogram of random tournaments

## Finding
For a uniformly random orientation of every edge of the complete graph on \(n\ge2\) labeled vertices, let \(D_i\) be vertex \(i\)'s number of outward edges and \(N_k=\sum_{i=1}^n\mathbf 1\{D_i=k\}\) its score-frequency counts, \(0\le k\le n-1\). Set \(b_k=2^{-(n-1)}\binom{n-1}{k}\), \(\Sigma_{k\ell}=\operatorname{Cov}(N_k,N_\ell)\), and
\[u_k=\sqrt{b_k},\qquad v_k=\frac{2(k-(n-1)/2)}{\sqrt{n-1}}\sqrt{b_k}.\]
Then \(u,v\) are orthonormal and
\[\boxed{\operatorname{diag}(b)^{-1/2}\Sigma\operatorname{diag}(b)^{-1/2}=n(I-uu^{\mathsf T}-vv^{\mathsf T}).}\]
For every \(n\ge2\), the complete whitened spectrum consists of \(n-2\) copies of \(n\) and two zeros. In particular, the binomial-reference Pearson statistic
\[Q_n=\sum_{k=0}^{n-1}\frac{(N_k-nb_k)^2}{nb_k}\]
has \(\mathbb E Q_n=n-2\), rather than the \(n-1\) expectation for a multinomial histogram with the same one-vertex marginal.

## Assumptions and scope
Each of the \(\binom n2\) matches has exactly one winner; its direction is sampled independently with probability \(1/2\) each way. All \(n\) vertex labels are distinct; no draws or ties are allowed. The result is exact for every integer \(n\ge2\), with no large-sample approximation. The covariance matrix has \(n\) entries on each axis corresponding to score levels \(0,\ldots,n-1\). The diagonal matrix \(\operatorname{diag}(b)\) is positive definite because \(b_k>0\) for each admissible level.

For arbitrary real-valued functions \(\phi,\psi\) on the score levels, put \(S_\phi=\sum_i\phi(D_i)\), and let \(B\sim\operatorname{Bin}(n-1,1/2)\). The equivalent functional form is
\[\operatorname{Cov}(S_\phi,S_\psi)=n\left[\operatorname{Cov}(\phi(B),\psi(B))-\frac{\operatorname{Cov}(\phi(B),B)\operatorname{Cov}(\psi(B),B)}{\operatorname{Var}(B)}\right].\]
This determines every mixed second moment of the score histogram. No joint normality, distributional identity with a conditioned multinomial, or asymptotic chi-square law is asserted.

## Proof
Write \(q=n-1\). The outdegree of one vertex is \(B\sim\operatorname{Bin}(q,1/2)\). For distinct vertices \(i\ne j\), condition on the single common match. The wins from their matches against the remaining \(n-2\) vertices are independent \(A,A'\sim\operatorname{Bin}(n-2,1/2)\), independent also of a fair Bernoulli \(E\). Thus \((D_i,D_j)\) has the law \((A+E,A'+1-E)\). With \(\Delta\phi(a)=\phi(a+1)-\phi(a)\), direct averaging over \(E\) gives
\[\operatorname{Cov}(\phi(D_i),\psi(D_j))=-\frac14\mathbb E[\Delta\phi(A)]\mathbb E[\Delta\psi(A)].\]
This is an exact identity for any score functions, with no independence assumption between the two outdegrees.

The binomial shift identity \(\mathbb E[B\phi(B)]=(q/2)\mathbb E[\phi(A+1)]\), together with \(\mathbb E\phi(B)=(\mathbb E\phi(A)+\mathbb E\phi(A+1))/2\), yields
\[\operatorname{Cov}(\phi(B),B)=\frac q4\mathbb E[\Delta\phi(A)],\qquad \operatorname{Var}(B)=\frac q4.\]
Sum covariances over \(n\) diagonal vertex pairs and \(n(n-1)\) ordered distinct pairs. The displayed functional formula follows exactly; the cancellation uses \(q=n-1\).

Choose \(\phi=\mathbf1_{\{k\}}\), \(\psi=\mathbf1_{\{\ell\}}\). Then \(\operatorname{Cov}(\phi(B),\psi(B))=b_k\mathbf1_{\{k=\ell\}}-b_kb_\ell\) and \(\operatorname{Cov}(\mathbf1_{\{B=k\}},B)=(k-q/2)b_k\). Therefore
\[\Sigma_{k\ell}=n(b_k\mathbf1_{\{k=\ell\}}-b_kb_\ell)-\frac{4n}{q}(k-q/2)(\ell-q/2)b_kb_\ell.\]
Whiten by multiplying on both sides by \(\operatorname{diag}(b)^{-1/2}\). The binomial mean and variance give \(\lVert u\rVert=\lVert v\rVert=1\) and \(u^{\mathsf T}v=0\). The matrix is \(n\) times the orthogonal projector onto the complement of the span of \(u,v\). Since that span has dimension two (also when \(n=2\)), the spectrum and rank follow.

Finally, linearity of trace yields
\[\mathbb E Q_n=\sum_k\frac{\operatorname{Var}(N_k)}{nb_k}=\frac1n\operatorname{tr}(\operatorname{diag}(b)^{-1/2}\Sigma\operatorname{diag}(b)^{-1/2})=n-2.\]
The two null directions correspond respectively to the deterministic identities \(\sum_kN_k=n\) and \(\sum_k kN_k=\binom n2\). The projector identity also proves there are no other nontrivial deterministic linear identities among score-frequency counts.

## Verification
The accompanying standalone `verify.py` enumerates all \(2^{\binom n2}\) labeled tournaments independently for each \(n\in\{2,3,4,5,6\}\). It accumulates complete score histograms and their pairwise products with exact rational arithmetic, then compares all \(90\) covariance entries with the derived closed formula. It also checks all score-level expectations and \(\mathbb EQ_n=n-2\) for each size. Run `python3 verify.py` with standard Python 3; it reports `VERIFY_OK` if all assertions hold. These finite tests are corroborative; the universal statement is proved algebraically above.

## Relationship to prior work
The fair random-tournament model and pairwise comparison statistics are classical. Cohn, Godbole, Harkness, and Zhang (arXiv:1502.04061v1, 2015), §§2–3, study counts of Seymour vertices. Their local score-threshold calculations condition on one common match and address asymptotic variance of a different count; they do not state a covariance law for arbitrary score functions or the full binomial-weighted histogram projector.

Alspach and Reid (1978) investigate *deterministic realizability* of degree-frequency sets in tournaments, rather than second moments of their random frequencies. Aldous and Kolesnik (2019/2022) study attainable **mean score vectors** under general tournament distributions and the Bradley–Terry model, not the covariance of the degree-frequency histogram of the independent fair model. The existence of general two-player joint-score representations in the wider paired-comparisons literature is a possible source of implicit coverage. The conclusion here is restricted to the exact projection, its full spectrum, and the Pearson expectation, not the novelty of conditioning on a common match itself.

## Limitations
The covariance projection says nothing about higher cumulants, the law of the score histogram, the distribution of \(Q_n\), or any asymptotic chi-square approximation. The parameter-free result applies only to independently and fairly oriented complete graphs; heterogeneous paired-comparison models may not satisfy it. Historical coverage of the exact projector has not been exhaustively ruled out, particularly in inaccessible early tournament-frequency literature.

## References
1. Z. Cohn, A. Godbole, E. W. Harkness, Y. Zhang, “The Number of Seymour Vertices in Random Tournaments and Digraphs”, arXiv:1502.04061v1 (first publicly submitted 2015-02-13), §§2–3.
2. B. Alspach, K. B. Reid, “Degree frequencies in digraphs and tournaments”, *Journal of Graph Theory* **2** (1978), 241–249, DOI:10.1002/jgt.3190020307.
3. D. J. Aldous, B. Kolesnik, “To stay discovered: On tournament mean score sequences and the Bradley–Terry model”, *Stochastic Processes and their Applications* **150** (2022), 844–852, DOI:10.1016/j.spa.2019.10.011 (first available online in 2019).
