# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. For centrally symmetric errors, each characteristic function is real and even; continuity, value one at the origin, and the nowhere-zero assumption force it to be strictly positive. Hence every observed edge-difference characteristic function is a positive product \(\Psi_{ij}=\varphi_i\varphi_j\), and real logarithms reduce the inverse problem pointwise to \(a_i+a_j=b_{ij}\).

The nullspace argument is exact. On a connected component, any null vector must alternate sign across edges. A bipartition supports a nonzero alternating vector, while an odd cycle forces the alternating value to equal its own negative and therefore vanish. Thus all error characteristic functions are uniquely recovered exactly when every component is non-bipartite. Characteristic-function uniqueness then yields distributional identification. Division by a recovered nonvanishing error characteristic function correctly recovers the latent characteristic function from one absolute measurement marginal.

Necessity was checked independently inside the Gaussian subclass: alternating variance shifts on the two parts of a bipartite component preserve every edge-difference distribution. When one absolute marginal is also observed, an opposite adjustment to the latent variance preserves that marginal as well while keeping all variances positive for sufficiently small perturbations.

The minimal-edge claim follows because each identifying connected component must contain a cycle and hence at least as many edges as vertices. A triangle with tree attachments attains equality for every \(m\ge3\). Exact rational verification enumerated every connected simple graph through six vertices and confirmed the rank/bipartiteness criterion on 27,475 graphs, including 24,226 non-bipartite cases. It also checked the triangle product identity and a Gaussian alias example.

## Originality

PASS, with a deliberately narrow claim. Classical three-cornered-hat work is not new: Gray and Allan (1974) explicitly derive individual oscillator variances from the three pairwise comparison variances, and modern three-cornered-hat and triple-collocation literature continues to develop second-order error-variance and covariance estimation. The rank characterization of an unsigned incidence matrix by bipartite components is standard graph linear algebra and is not claimed as a contribution.

Kotlarski's repeated-measurement theorem identifies latent and measurement-error distributions from the full joint law of repeated measurements, which is strictly richer than selected pairwise-difference marginals. Nearing et al. (2017) develop a nonparametric information-theoretic extension of triple collocation but describe the general full measurement problem as underdetermined. Spicker (2024) explicitly treats symmetric independent replicate errors, including non-identically distributed replicates, to construct contrast-error distributions for nonparametric SIMEX; the inspected sections do not give separate reconstruction of every heterogeneous error law from edge-difference marginals or an odd-cycle graph criterion. Ellis (2002) proves nonuniqueness for a single convolution with an unknown symmetric factor, which is adjacent blind-deconvolution context rather than the linked multi-convolution result here.

Searches covered three-cornered-hat and M-cornered-hat methods, triple/extended/nonparametric collocation, repeated-measurement deconvolution and Kotlarski identities, symmetric blind deconvolution, pairwise-difference distributions, sparse/incomplete comparison designs, edge-product factorization, and unsigned-incidence identifiability. No located source states the claimed distribution-level odd-cycle equivalence, sharp bipartite Gaussian alias, and exact minimal comparison design together or separately in this measurement-error setting.

The full theorem text of Grubbs (1948), an early precision-of-instruments source cited by modern three-cornered-hat histories, was not inspected directly; modern accounts characterize that line as variance estimation. Older metrology, calibration, deconvolution, and replicate-measurement literature may contain an equivalent factorization under different terminology. Because the proof is elementary once written in characteristic-function form, this is the principal residual originality risk.

## Value

PASS. The result upgrades the familiar variance-level three-cornered-hat idea to complete nonparametric error distributions and gives an exact sparse-design boundary. It shows that a triangle is not special because there are three instruments: the essential object is an odd cycle, and a single odd cycle plus tree attachments identifies arbitrarily many heterogeneous error distributions. Conversely, a tree or any bipartite comparison component has a genuine continuum of observationally equivalent smooth Gaussian models.

The theorem also separates data requirements cleanly. Pairwise difference marginals identify the error laws under the graph condition without requiring the full joint distribution of all instruments; after that, one absolute measurement marginal is sufficient to identify the latent distribution. This can inform sparse calibration designs when full simultaneous multichannel joint data are unavailable or unnecessarily expensive.

## Limitations

The theorem assumes additive collocated measurements of a common latent quantity, mutually independent errors, known zero centers, central symmetry, and nowhere-zero error characteristic functions. It is structural identification, not an estimator or finite-sample stability theorem. Near zeros, characteristic-function logarithms can be numerically unstable.

Nonsymmetric errors introduce complex phases and are not covered. Characteristic-function zeros, correlated errors, nonadditive observation maps, and pairwise comparisons formed from different latent quantities require separate analysis. Full joint repeated-measurement data can identify models under different assumptions, so the result should not be read as a replacement for Kotlarski-type identification.
