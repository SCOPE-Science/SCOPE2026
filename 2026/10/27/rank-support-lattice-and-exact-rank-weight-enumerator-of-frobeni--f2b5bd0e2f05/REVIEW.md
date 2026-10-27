# Scientific review

## Correctness (C): PASS

The orbit-seed representation follows from the source paper's finite-abelian Fourier descent. With a normal basis, Frobenius gives the cyclic module \(\mathbb F_q[T]/(T^d-1)\), *even if* characteristic divides \(d\). The submodule with annihilator \(f\) is precisely \(\ker f(\sigma)\), with dimension \(\deg f\). The sum of conjugate-generated seed submodules has annihilator their least common multiple. In each primary factor, the count of independent seed tuples with maximum annihilator exponent bounded by \(j\) is \(q^{\delta_P\sum_i\min(j,a_{iP})}\); finite differences and CRT reconstruct every coefficient. A full-length Frobenius orbit guarantees each allowable exponent is attained. Direct enumeration checked six complete cyclic cases and one complete noncyclic character transform. No finite check is treated as a proof for all fields.

## Originality (O): PASS with identified residual risk

The closest primary full text, Kumallagov–Sizikov–Zarubin arXiv:2605.20062 (Theorem 3.1 and Propositions 8.1–8.2), gives independent orbit seeds and a **symbol Hamming** enumerator, not the rank support of spectral values or its multiplicities. The checked q-order literature arXiv:2601.09201 defines one-element Frobenius order and normality, while the claim requires the entire joint multi-orbit primary-decomposition distribution. Mathematically these antecedents supply ingredients but do not state the code-level enumerator or individual-support counts. Targeted mathematical-record and literature searches found no dominating theorem. Classical cyclic-module enumerator technology could imply an equivalent formula under another name; unindexed or implicit coverage remains a real priority risk. No independent priority certification is asserted.

## Value (V): PASS

The natural field-value rank metric is distinct from the source paper's positional Hamming measure. The theorem determines the **entire exact support lattice** and the population of every Frobenius-invariant support in all finite abelian cases, not a small numerical parameter. The characteristic-dependent repeated-root behavior, explicit all-rank probability and finite factorization recipe provide a useful structural benchmark for rank-metric behavior and spectral diversity in this new code family. No coding-rate or decoder-performance improvement is asserted.

## Sources and limitations

Primary sources: arXiv:2605.20062 (full Theorem 3.1, Proposition 8.1–8.2 and residual-coding sections read), arXiv:2601.09201 (Frobenius-order preliminaries and section 3 read). General finite-field normal basis results and the 2013 k-normal line of work are classical antecedents. All computations and their exact small-case limitations appear in `VERIFICATION.md` and the standalone verifier.

Self-review: passed. Independent audit: not yet performed.
