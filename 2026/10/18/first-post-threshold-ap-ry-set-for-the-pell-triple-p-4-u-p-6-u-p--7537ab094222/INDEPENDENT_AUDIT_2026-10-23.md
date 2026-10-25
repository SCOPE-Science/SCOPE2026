# Independent mathematical audit

## correctness

PASS

For u>=2, put s=u²+2, p=u², a=us, b=u(s²-1), c=P9(u)=(s²-s-1)(s²-1)-s(s-1) and h=s-1. The proved identities include gcd(a,b,c)=1, c≡1 mod u and c+sh=qv<2c. On a candidate T=(ps+j)b+zc, 0<=j<s and 0<=z<u, reduction mod u forces any representation's c-count Z=z+ut and the size bound forces t∈{0,1}. The t=0 equations have p+1 solutions at T, p after subtracting any positive k<=s copies of a; the t=1 branch contributes exactly one extra solution when j=s-1 and k<=h, yielding the single exceptional row subtraction ha. The a=us residues are all represented exactly once; monotonicity of denumerants upon adding a proves minimality. Summing Apéry elements gives n_p, and max-a gives g_p. Independent generating-function dynamic programming for u=2,3,4 reproduced exact Apéry thresholds and (g,n)=(2943,2332),(64817,50364),(687391,530288); this does not replace the all-u proof.

## originality

PASS

Best-of-knowledge original contribution is the precise First beyond-published-range p-Apéry set and corrections at p=u² for Pell triple (P4,P6,P9). Prior coverage of general methods/nearby problems is credited; exact statement/implication comparisons and residual risks are detailed below. The unsuccessful Resultary lookup is not treated as proof of novelty.

## value

PASS

The boundary p=u² is the very first excluded index of the published uniform Pell-triple formulas, and naive rectangular extrapolation gives objectively wrong genus and Frobenius numbers. Exactly identifying u changed residues and corrections (s-1)a and u(s-1) explains the structural phase change for a natural recurrence triple. This is a motivated precise threshold fact, not a random substitution into a known case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
