# Independent mathematical audit

## correctness

PASS

With exactly \(m\) nonnull streams and all null e-values frozen at one, terminal full discovery cannot have e-BH rank above \(m\): for every rank \(r>m\), the \(r\)-th ordered value is one while the threshold \(K/(\alpha r)>1\). Thus full discovery forces rank exactly \(m\), and every nonnull terminal value must be at least \(b_m=K/(\alpha m)\). Therefore stream \(i\) must receive at least its own first-passage count \(\tau_i\); summing gives the pathwise lower bound. Sampling each nonnull until first crossing and then parking it attains the bound, because the \(m\) parked values all meet the rank-\(m\) cutoff. If every parked value is lowered below \(b_m\), the rank-\(m\) condition fails, proving sharpness of the common boundary. For likelihood-ratio streams, Wald's identity under the stated integrability assumptions yields \(D_i\mathbb E\tau_i=\log b_m+\mathbb E O_i\), giving the expectation formula. The inspected exact-rational verifier implements rank-geometry checks and a nonmonotone path example; the general result follows from the rank argument above.

## originality

PASS

After open arXiv routes failed in this run, the primary Lin--Ma--Ren--Wei preprint was obtained through authorized institutional access and materially read through the e-BH definition, the full-discovery upper/lower results, simple likelihood-ratio specialization, and the expected-stopping appendix. Its nonnull upper analysis uses individual crossing level \(\log(K/\alpha)\), while Theorem 4.2 gives an information lower scale \(\log(1/\alpha)\); Appendix B likewise defines nonnull first passage at \(\log(K/\alpha)\). It does not identify the exact oracle pooled boundary \(K/(\alpha m)\), the exact pathwise sum of multiplicity-sensitive first passages, or the sharp parking theorem. Resultary searches for that formula found no equivalent published record. The claim is therefore original at the narrow oracle-benchmark level, not as a broad new e-BH procedure.

## value

PASS

The theorem isolates a motivated benchmark in the exact full-discovery problem studied by the current source. The threshold \(\log(K/(\alpha m))\) interpolates between the one-signal \(\log(K/\alpha)\) boundary and dense-signal \(\log(1/\alpha)\) scale, separating step-up multiplicity pooling from the extra cost of identifying signals and maintaining live evidence. The exact pathwise optimum and overshoot-aware expectation are therefore useful structural benchmarks despite the deliberately oracle-favorable assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
