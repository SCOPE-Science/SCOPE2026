# Independent mathematical audit

## correctness

PASS

For all N>=1, r>d>0, p_i>0 and initial 0<T<=1, P=sum p_i x_i x_{i+1}<=p_*T^2, hence logistic comparison yields uniform T>=min(T0,(r-d)/(r+p_*)). If m=min initially occupied site then u_i=x_i/x_m are decreasing, x_m/T bounded below, and clock tau=int_0^t x_m ds >= delta t. The triangular exact system du_i/dtau=-p_{i-1}u_{i-1}u_i determines by induction whether u_i has positive limit (preceding absent/decays) or decays exponentially (preceding positive), giving the greedy support with no dependence on magnitude of positive p_i. P(t) decays, logistic relaxation gives T->K=1-d/r exponentially, and each x_i tends exponentially to the claimed equilibrium. For N=3 integrate u_2 in tau to obtain R and exact limiting abundances. Independently solved N=3 IVP and matched exact limit to 1.4e-12; not a proof. No convergence statement when demographic rates differ or p_i=0.

## originality

PASS

PASS (best of knowledge): Samanta et al study the same hierarchical directed model and establish only independent-set equilibrium restrictions and transverse/numerical observations; a stable independent set is not the trajectory-selected greedy independent set. The exact triangular time-change proves global convergence from every nonzero nonnegative initial state, initial-support selection, exponential rate, and abundance split. Baigent–Ching attract a continuum and Hou assumes a unique common attractor; neither implies the history-dependent all-N result. Standard competitive triangular techniques may overlap in older unindexed literature, recorded as risk.

## value

PASS

PASS: The source paper identifies coexistence-compatible independent sets without deciding which one a trajectory reaches. A global all-N greedy support rule and exact surviving abundances solve a meaningful selection problem for the specified deterministic ecological chain, including arbitrary positive predation rates and boundary initial supports. The rate of convergence is not uniform over initial states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
