# Scientific review

## Correctness — PASS
The binary addition automaton has explicitly derived transition matrices for both digits of the fixed shift. The geometric tail is normalized and the reference matrix product is evaluated exactly. The rank-one zero-gap perturbation starts in degree \(h_i+1\), and the single-boundary coefficient is \(-2^{-2r}\); all multiple perturbations enter after degree \(r\). Negative-binomial extraction and Kummer's carry identity give the claimed probabilities for every \(r\ge1\), including \(r=1\). Exact rational Markov computations and separate finite dyadic counts reproduce the formulas on selected finite domains. No finite test is presented as an infinite proof.

## Originality — PASS, with residual risk
Full-text comparisons were made with the theorem statements and relevant methods of Cheng, arXiv:2608.25899; Sobolewski–Spiegelhofer, arXiv:2411.07779; and Drmota–Kauers–Spiegelhofer, arXiv:1509.08623. Existing matrix recurrences allow numerical calculation for any fixed shift; this observation is distinguished from an explicit arbitrary-rank finite-gap plateau with an exact first-contact correction for heterogeneous gaps. The strongest nearby results describe asymptotic fixed-weight minima and extended infinite-block behavior, rather than the formula here. The broad generality of earlier recurrences is a genuine source of implicit-coverage risk, and the full text of Cheng's earlier first-exit paper could not be read.

## Mathematical value — PASS
The finite-gap shielding criterion and its sharp first-contact defect answer a natural structural question: precisely how far separated active binary digits must be before the nonnegative part of their carry interaction decouples. The answer holds at all Hamming weights, gives a complete layer-by-layer law up to the natural cutoff \(r\), and quantifies the first failure by a local geometric count rather than by a numerical catalogue. It supplies a family-wide exact companion to recent fixed-weight asymptotic investigations, without claiming a new proof of Cusick's general conjecture.

## Limits and sources
Source identifiers: arXiv:2608.25899; arXiv:2411.07779; arXiv:1509.08623; arXiv:2005.07167. The result is restricted to shifts whose successive set-bit positions differ by at least their Hamming weight. Priority over unindexed explicit formulas remains unverified.

Self-review: passed. Independent audit: not yet performed.
