# Independent mathematical audit

## correctness

PASS

For all k≥2, a,d>0 and t>0, factor e^{-aℓt} from each pair of rows, subtract a times the amplitude row from the decay-slope row, divide by d and remove a factor x_ℓ=q^ℓ. The resulting paired polynomial value/derivative matrix is the standard confluent Vandermonde; its pairwise |x_r−x_ℓ|^4 factors and geometric-node powers give exactly d^k q^{k(k−1)(a/d+(4k−5)/6)}∏_{h=1}^{k−1}(1−q^h)^{4(k−h)}. The formula is nonzero for q∈(0,1), so full state recovery and minimal k time slots follow. Fixed iid variance gives det I=σ^(−4k)|det H|². The log determinant derivative equals β_k−4Σ h(k−h)q^h/(1−q^h); the sum increases strictly from 0 to ∞, so there is one interior maximum, with determinant zero at both endpoints. For fixed α=a/d>0, c_k=−k log q_k satisfies β_k/k³=(4/k)Σ f_{c_k}(h/k), f_c(x)=x(1−x)/(exp(cx)−1), f_c(0)=1/c. Uniform O(1/k) Riemann-sum error on compact positive c and the strictly negative derivative of 4∫f_c give c_k=c_*+O_α(1/k), c_* unique with 4∫f_{c_*}=2/3, and the stated horizon. k=2 reduces to q=(2a+d)/(2a+5d). Independently recomputed 24 distinct exact rational determinant cases and high-precision root convergence, without using finite checks as proof of all k.

## originality

PASS

The full constrained conclusion—an exact 2k-mode/two-simultaneous-sensor equally spaced Fisher determinant, a unique optimal spacing for every k and a fixed-offset universal asymptotic horizon—is not implied by the inspected generic delay-representation, Hermite interpolation, or exponential-regression design theorems. The determinant factorization is classical confluent Vandermonde and is excluded from novelty by itself. Targeted published-record searches found this same finding but not another distinct source covering the combined extremum and limit. Best-of-knowledge PASS with residual priority risk from older design literature.

## value

PASS

In a natural stable linear inverse problem with an entire family of arithmetic decay spectra and two physical amplitude/decay-slope sensors, mere observability does not specify experiment timing. The exact Fisher determinant, unique global optimum within equal meshes for every size, and nontrivial spectral-gap-scaled universal finite limiting observation horizon provide a motivated quantitative design result; a researcher could use the exact q_k equation and asymptotic constant to select/benchmark observation windows for growing mode count. This goes beyond a renamed generic matrix determinant, finite table, or cheap normalization check, while explicitly not claiming unconstrained globally D-optimal time grids or a general flow theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
