# Independent mathematical audit

## correctness

PASS

For fixed α>1 and specified Pozsgay permutation gate and normalized one-site transition or domain-wall state (infinite-volume limit first), group the count-resolved coefficient matrix by difference d=ℓ-k. At fixed d, branch matrices occupy mutually orthogonal count rows/columns, so ||M_d||_(2α)^(2α)=2^((1-α)g(d)) Σ_k(q_k r_(k+d))^α. Uniform binomial peak and overlap bounds make the sum at most Oα(t^(1/2-α)); g(d)>=|d|-1 gives a convergent geometric factor across d. Schatten triangle yields the global upper bound. Count-diagonal phase pinching is contractive and, using g(0)=0 and the local central binomial lower bound for Θ(sqrt(t)) central k, yields a matching Ωα(t^(1/2-α)). Therefore Zα=Θα(t^(1/2-α)) and Sα=((α-1/2)/(α-1))log t+Oα(1). I checked that this does not assume cross-difference orthogonality. Independent binomial overlap computations corroborated asymptotic scaling; finite checks are not the infinity-time proof.

## originality

PASS

Best-of-knowledge original narrow result after comparing actual mathematical implications with primary source and adjacent literature: Source derives the exact individual branch spectra but only Θ(log t) for full high-index entropies; the audited matched upper/lower control on coherent assembly supplies the numeric coefficient. No claim of novelty of the gate, flat spectrum, or source's rough growth theorem.

## value

PASS

The originating integrable circuit paper isolates high-index logarithmic growth but leaves its coefficient uncalibrated. A sharp coefficient for both operator and domain-wall entanglement at every fixed α>1 closes a natural open quantitative invariant using a reusable count-diagonal Schatten pinching argument. This is not a mere normalization, recasting, or numerical prefactor tweak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
