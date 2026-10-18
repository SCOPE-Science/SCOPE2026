# Independent mathematical audit

## correctness

PASS

At epsilon=1, the original channel multiplies Fock coherence (m,n) by q^{(m-n)^2}, q=e^{−t}. The proposed input has energy 3/2 and output eigenvalues 0,(1−q)/2,(1+q)/2. For K=2,N=3/2 the only binomial has M=2, mu=3/4; farthest-separated inputs have fixed probabilities 1/4 and 3/4, any phase. Independent exact symbolic polynomial calculations give P_B=(9q^8+60q^2+59)/128 and P_kappa=(3q^8+5)/8; set L=(1+q)/2, T=L^2+(1−L)^2/2=(3q^2+2q+3)/8. Both gaps factor as (1−q) times polynomials strictly positive for 3/4<=q<1, so purities <T and largest eigenvalues <L. The entropy of any qutrit density with λmax<L exceeds h2(L): for λmax>=1/2, splitting its remaining weight only increases entropy; for λmax<1/2 its entropy >1>h2(L). The witness entropy is exactly h2(L), hence strict inequality throughout. Independently checked symbolic factorization and four rational q values, including exact endpoint binomial purity 6137513/8388608, farthest purity 347363/524288 and T=99/128. The proof is analytic; no claim of global optimization.

## originality

PASS

The original 2016 paper contains the conjecture and analyzes a different K,N example numerically; the witness lies outside both candidate families and contradicts that conjecture on a nonempty interval. Later bosonic dephasing papers address coherent information or quantum capacity, not this fixed-energy minimum output entropy. No published equivalent counterexample was found in web/Resultary searches. The 2016 primary text was actually read; still best-of-knowledge for all later literature.

## value

PASS

A closed-form rigorous counterexample to a named published conjecture is a substantive mathematical correction to the proposed optimizer families, with an entire parameter interval and a simple qutrit witness. It pinpoints an overlooked adjacent-Fock-level mechanism rather than an arbitrary numerical exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
