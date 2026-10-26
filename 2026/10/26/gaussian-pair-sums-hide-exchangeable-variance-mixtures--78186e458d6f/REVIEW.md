# Scientific review: Gaussian pair sums hide exchangeable variance mixtures

## Correctness (C): PASS

Conditioning on \(V\) makes the pair sum a centered normal with variance \(1-2V+2V=1\). Conditional iid sampling given \((V,Z)\) establishes infinite exchangeability. The marginal variance and pair covariance depend only on \(\mathbb EV\); the fourth-cumulant identity \(3\operatorname{Var}(V)/4\) proves non-Gaussianity for every non-point mixing law. The pair-difference characteristic function is the Laplace transform of \(\rho\), which is unique on bounded support. The explicit rational example is checked by the included standard-library script.

## Originality (O): PASS, with residual priority risk

The closest primary result is Zheng–Zhou’s theorem that joint Gaussianity of one pair forces an infinite exchangeable sequence to be Gaussian. That theorem assumes the full pair is jointly Gaussian; it does not imply that a single Gaussian linear projection plus second-order covariance data identifies the pair law. Evans–Zhou establish the broader, classical failure of identifying exchangeable sequences from all partial-sum laws in general, but their inspected counterexample does not provide this exact Gaussian pair-sum family or the difference-Laplace recovery. Targeted semantic and literature searches found no direct match. A similar construction under another name may exist; the novelty claim is restricted to the explicit Gaussian sum/covariance-matched family and its identifying difference law.

## Value (V): PASS

The construction gives an exact diagnostic boundary for Gaussian rigidity: the pair-sum law and the entire covariance matrix can coincide for a Gaussian process and a non-Gaussian infinite exchangeable process. It also gives a natural identifying contrast within the family, since pair differences recover the latent mixing law by a Laplace transform. The result is a reusable all-parameter family, not a finite simulation or a claim that one example settles arbitrary exchangeable models.

## Closest literature and limitations

The result does not classify all exchangeable processes with Gaussian pair sums and does not produce a non-Gaussian process with Gaussian one-dimensional marginals. The full joint law of overlapping pair sums is not asserted to be the same across mixing laws.

Self-review: passed. Independent audit: not yet performed.
