# Same-model review

## Correctness

**PASS.** In the source normalization, the input, output, and uniform-rest sector is exactly three-dimensional. With the mean endpoint shift fixed at \(2n-6\), differential detuning produces a reduced matrix with eigenvalues \(0,\pm\Omega\). The identity \(M^3=\Omega^2M\) gives the propagator explicitly, and the transfer probability is a positive constant times \([1-\cos(\Omega t)]^2\). This proves both the global maximum and all maximizing times. A standalone replay checks the reduction and the closed probability formula.

## Originality

**PASS, narrowly scoped.** The direct source solves equal endpoint shifts exactly and treats random frequency or coupling disorder numerically. Its exact fidelity formulas assume one common endpoint shift and therefore do not cover the unequal-endpoint Hamiltonian used here. Targeted searches for unequal endpoint shifts, antisymmetric detuning, endpoint frequency mismatch, and complete-graph-minus-edge transfer did not locate the closed maximum-fidelity law. Later robustness work studies optimized spin-ring controllers and sensitivity measures rather than this exact family.

The claim does not take ownership of the missing-link graph, the optimal equal shift, or the source's perfect-transfer result.

## Value

**PASS.** Differential endpoint calibration is a natural control imperfection precisely because the ideal protocol requires equal endpoint energies. The theorem replaces a qualitative statement that asymmetry harms transfer with an exact global fidelity ceiling, exact readout times, and a target-dependent tolerance window. The \(\sqrt n\) tolerance scale identifies how the calibration budget changes with network size.

Same-model review: passed. Independent audit: not yet performed.
