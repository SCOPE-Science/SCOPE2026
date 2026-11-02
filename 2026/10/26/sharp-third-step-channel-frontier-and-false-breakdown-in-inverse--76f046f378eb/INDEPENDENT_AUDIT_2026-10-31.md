# Independent mathematical audit

## correctness

PASS

From beta v2=A^{-1}v-alpha v, applying A gives beta A v2=v-alpha A v. Q kills v, hence the exact residual identity QAv2=-(alpha/beta)QAv for arbitrary invertible real A with beta>0 and QAv nonzero; symmetry is nowhere needed. Norming the respective candidates yields gamma_3=|alpha|sqrt(m2)/sqrt(1-2alpha m1+alpha² m2), whose positive denominator is beta||A v2||. Therefore gamma_3²-1=(2alpha m1-1)/(1-2alpha m1+alpha² m2) gives exact all-three comparisons, including gamma=0 at alpha=0. Independently checked rational A=diag(-6/5,2,3), v=(1,1,1)/sqrt3: alpha=0,beta²=19/54,det[b,A^-1b,Ab]=28/15,||QAv||²=1568/4275, cond(A)=5/2. The nonzero determinant certifies space nonexhaustion; n=3 is minimal for a possible third independent direction. Starting b=(1,1,2) and (1,2,2) give alpha m1=16/45,47/81; analytic differentiation at the perturbed A_t yields gamma/|t|->95/(108sqrt3). Fresh exact SymPy verifies the witness and both sign regimes. Earlier finite experiments from assigned code do not substitute for the elementary all-matrix algebra.

## originality

PASS

PASS, qualified: the residual proportionality is elementary and already present in the main 2026 source recurrence, so is explicitly credited. The assessed new result is the exact normalized all-real-matrix third-step ordering, full-rank minimal 3×3 false breakdown and bounded-condition-number near-breakdown slope. Earlier full texts of classic extended Krylov papers were not obtained.

## value

PASS

Different operator channels are standard implementation choices. A recurrence that breaks at the minimal third vector even when the exact extended Krylov space continues to grow is an algorithmically meaningful pathology. Its existence with spectral condition 5/2 and a sharp all-real-matrix comparison frontier has diagnostic value beyond simply rewriting an existing recurrence; it precisely limits the definite-matrix stability intuition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
