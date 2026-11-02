# Scientific review: joint Bernoulli-tree hitting-time limit

## Correctness

**PASS.** The statement distinguishes tree randomness from random-walk path randomness, fixes the exact finite-tree model and both hitting-time directions, and uses the correct centering and normalization. Exact deterministic component-count and commute identities reduce the first-passage means to the inverse-renewal count and its integral, with a pathwise error controlled by the longest run of second-predecessor attachments. The tail bound for that longest run makes the error negligible on the \(N^{3/2}\) scale. Donsker inversion gives the claimed joint Brownian functional, and direct Brownian covariance calculations yield the matrix and its \(1/2\) off-diagonal correlation. The accompanying script checks all finite attachment histories through size twelve and independently solves rational hitting-time systems through size seven; its finite checks are not used as a substitute for the limit proof.

## Originality

**PASS, with historical-priority risk.** The exact Bernoulli predecessor tree is analyzed by Tang--Wang--Wu for ends and collisions, rather than the joint root-to-newest first-passage mean fluctuations. The general deterministic graph-hitting identities are known and expressly credited to classical theory and Georgakopoulos--Wagner. Standard renewal FCLTs likewise are known. The specific approximation of tree hitting means by the integral of the same backward ancestry renewal process, and the resulting joint covariance including universal half-correlation, were not found in the examined sources or mathematical-record comparisons. Oosthuizen--Wagner treats random-tree hitting-time laws for different tree ensembles and scales; only its abstract was available, leaving an explicit residual risk. No independence or definitive priority claim is made.

## Mathematical value

**PASS.** The source model's existing qualitative collision result does not quantify search latency. The joint first-passage limit establishes the sharp magnitude of conditional search costs and their random-geometry fluctuations, including how the two orientations cofluctuate. The same Gaussian variance in both directions and the nontrivial parameter-independent correlation are natural structural properties of this exact model, not an arbitrary choice of a small numerical slice.

## Scope and unresolved limitations

The theorem is specific to finite Bernoulli recursive trees, fixed interior attachment probability and tree-conditioned *means*. It makes no assertion about the random first-passage time distribution along an individual trajectory, nor about universality over other attachment rules. The cited tree-hitting formula and inverse-renewal invariance principle are established inputs. A full historical-priority check outside the inspected literature remains appropriate.

Self-review: passed. Independent audit: not yet performed.
