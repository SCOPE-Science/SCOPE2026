# Independent mathematical audit

## correctness

PASS

For household size four and Exp(1) infectious periods, use q_j=(1+j ell)^-1, the exact Ball et al. beta_k/mu_k recurrences and triangular first-epidemic P_v recursion. For s=sum((4-v)P_v/4), U_v=C(4,v)(1-s)^v s^(4-v), and D=sum_{v=0}^3((4-v)/4)(P_v-U_v)mu_(4-v), independent SymPy algebra from those recurrences produced D=ell^2 pi^2(1-pi) H / [(1+ell)^15(1+2ell)^10(1+3ell)^5]. Independently reconstructed H has bidegree (13,28), and its 14x29 Bernstein-by-ell coefficient table has 403 strictly positive and 3 zero exact rational entries, no negative entries and no identically zero row. Generated UTF-8 TSV is 5925 bytes with Git blob SHA 5e8f08634a64383b469aa1c1eaca20379ff9b2b4, EXACTLY matching the pinned package's coefficient file, so all 406 coefficients and the polynomial identity are verified, not just the verifier log. A separate exact CTMC recursion at ell=1,pi=1/2 yields P=(1/16,1/16,1/16,7/64,45/64), mu=(1,3/2,13/6,143/48), and D=10262378043/68719476736>0. Bernstein positivity for ell>0 and 0<pi<1 proves the universal finite-Markovian n=4 inequality. The herd-immunity corollary follows from strict monotonicity of the vaccination threshold; it concerns tilde h_D, not the unrestricted h_D.

## originality

PASS

The complete Ball--Critcher--Neal--Sirl (J Math Biol 2023) PDF was inspected at Theorem 4.11, Conjecture 4.12, Fig 6, and Appendix B.3; it analytically covers n=2,3 and leaves n>=4 conjectural, with only numerical illustrations and asymptotic small/large contact statements for n=4. The exact 406-coefficient positivity certificate resolves n=4 for all positive finite rates under exponential infectious periods. Other Resultary household threshold/ranking and vaccination records concern different observables and do not imply this strict DI vs U comparison. No stronger all-n proof was found in the searched sources; unindexed work remains a risk.

## value

PASS

The first open household size of a precisely published conjecture is a natural finite cutoff, and the proof covers the full two-parameter positive domain rather than extrapolating simulations or low-contact perturbation. The rational Bernstein certificate is nontrivial and enables future extension or falsification attempts for larger or non-Markovian households.

The dated certificate retains the supplied scientific assessment, sources and limitations.
