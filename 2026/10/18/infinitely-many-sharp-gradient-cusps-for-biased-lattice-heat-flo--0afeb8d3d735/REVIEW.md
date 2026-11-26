# Independent mathematical audit

## correctness

PASS

The independent Poisson jumps give the stated Skellam kernel; a sign input at one edge attains the ℓ¹ sum of the shifted kernel differences. The strict shape used to telescope that sum can also be checked without a Turán citation: R_j=I_{j+1}/I_j starts as z/[2(j+1)] and solves R_j'=1−(2j+1)R_j/z−R_j². A first contact of R_j with R_{j+1} from above is impossible because the derivative difference at contact is 2R_j/z>0. Also R_j lies below the increasing positive Riccati nullcline, by its initial slope and a first-contact comparison, so R_j'>0 and R_0<1. This gives strict log-concavity on both halves and across index zero, hence the telescoping norm 2 max p_t. For a>b, reflection of the mass excludes negative modes; the ratios increase from 0 to √(a/b)>1 and strictly decrease in j, and the defining series gives R_j≤z/[2(j+1)] at fixed z. This proves unique ordered switches escaping to infinity. Differentiation at a tie gives 2p_t(k)r'_k(t)=4a p_t(k)R'_k(2t√(ab)); the symmetric case has a single analytic branch. For the asymptotic, put u=√t θ and y=k−(a−b)t. The real part of the phased difference factor on |u|≤t^{1/10} is −[(y+1/2)u²+(a−b)u⁴/6]/t plus a bound of t⁻² times a fixed polynomial in |u|, uniformly in bounded y. Replacing the cosine weight by exp(−(a+b)u²/2) costs O(t⁻¹) times a Gaussian-weighted polynomial before multiplication by the O(t⁻¹) difference factor; the complement is exponentially small. The second and fourth Gaussian moments give the bracket y+1/2+(a−b)/[2(a+b)]+O(t⁻¹). Bracketing the unique zero at t=(k±C)/(a−b) and inserting it in that uniform estimate gives the stated O(k⁻¹) in time. Reflection exchanges rates; the time locations depend on the sum as well as on the drift magnitude, and no drift-uniform claim is made. The finite checker was inspected but not executed; it is not required for the analytic proof.

## originality

PASS

The Skellam representation, Bessel ratio tools, and unimodal total-variation identity are ingredients, not distinct claims to priority. The supported contribution in the inspected comparison is the biased sharp-norm switching law with strict derivative discontinuities and the fixed-rate two-term switching-time expansion. The closest indexed staircase has a different norm, symmetric rates, and a different switch equation.

## value

PASS

For a natural endpoint smoothing norm, sharpness and its time regularity are different issues. The theorem identifies an extremizing sign input and gives a full nonsmoothness law caused by arbitrarily small fixed nonzero drift, contrasting with the symmetric analytic norm even though individual kernel coefficients stay analytic. The quantitative correction locates these corners more precisely than the mean drift of the walk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
