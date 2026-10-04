# Boundary-corrected positivity and exact mass conservation in the Liu–Tian SEIR step
## Finding
Liu and Tian's forward SEIR update in their equation (3.1) is unconditionally nonnegativity preserving and, more strongly, exactly preserves the total accounted population \(P=S+E+I+R+D\) when the demographic terms are set to zero as in their numerical section. Its printed strict-positivity statement is too strong: a boundary state need not enter the interior.

Precisely, assume \(h>0\), \(\beta^k,\epsilon^k,\gamma^k,\mu^k\ge 0\), and \(N^k=S^k+E^k+I^k+R^k>0\). If \(S^k,E^k,I^k,R^k,D^k\ge0\), then equation (3.1) gives \(S^{k+1},E^{k+1},I^{k+1},R^{k+1},D^{k+1}\ge0\) and
\[
S^{k+1}+E^{k+1}+I^{k+1}+R^{k+1}+D^{k+1}
= S^k+E^k+I^k+R^k+D^k.
\]
The implication with a strict \(>0\) conclusion fails, for example, at the disease-free state \((N,0,0,0,0)\), which is left unchanged by the update.

## Assumptions and scope
The statement concerns only the forward discretization used in Section 3.1 of the cited work, where the authors set birth and natural-death parameters to zero. It assumes the denominator \(N^k\) is the living population \(S^k+E^k+I^k+R^k\), as in the model definition, and that \(N^k>0\). No claim is made here about convergence order, the backward co-state solver, the outer optimization iteration, or epidemiological validity of fitted parameters.

## Proof
Introduce the nonnegative step transfers
\[
F=h\beta^k S^{k+1}I^k/N^k,\qquad
G=h\epsilon^k E^{k+1},\qquad
H=h(\gamma^k+\mu^k)I^{k+1}.
\]
Because all denominators in equation (3.1) are of the form \(1+hq\) with \(q\ge0\), the sequential formulas immediately give nonnegative updated components from nonnegative inputs.

Rearranging the five update equations gives
\[
S^{k+1}-S^k=-F,
\]
\[
E^{k+1}-E^k=F-G,
\]
\[
I^{k+1}-I^k=G-H,
\]
\[
R^{k+1}-R^k=h\gamma^k I^{k+1},\qquad
D^{k+1}-D^k=h\mu^k I^{k+1}.
\]
The last two increments sum to \(H\). Adding all five identities therefore cancels \(F\), \(G\), and \(H\) exactly, proving conservation of \(P\). It also shows \(D^{k+1}\ge D^k\).

For the boundary issue, take \(S^k=N>0\) and \(E^k=I^k=R^k=D^k=0\). Then every transfer vanishes and equation (3.1) returns the same state. Hence the paper's displayed implication from componentwise nonnegativity to componentwise strict positivity is false without additional assumptions. The corrected unconditional conclusion is componentwise nonnegativity.

## Verification
The accompanying `verify.py` replays equation (3.1) with exact rational arithmetic on representative nonnegative states, checks the conservation identity exactly, verifies monotonicity of \(D\), and checks the disease-free boundary counterexample. These computations supplement, but do not replace, the algebraic proof above.

## Relationship to prior work
The source explicitly motivates equation (3.1) as an unconditional positivity-preserving discretization and states \(U^k\ge0\Rightarrow U^{k+1}>0\). A text search of the source did not locate a stated conservation law for this update. Searches of the available finding database for this specific SEIR discretization, its boundary behavior, and exact mass conservation did not locate the same statement; the closest results concerned different positivity-preserving schemes or different epidemic models. General structure-preserving epidemic discretizations are known in the literature, but that does not imply this exact telescoping identity or repair the strict boundary claim for equation (3.1).

## Limitations
This is a correction and structural invariant for one numerical step, not a claim that the paper's epidemiological conclusions or optimization results are false. The literature search cannot prove absolute novelty, and a conservation observation could exist in material not indexed by the searched services. The result is nevertheless directly checkable from the published formula and gives a sharp boundary statement plus an implementation-level invariant.

## References
1. H. Liu and X. Tian, “Data-driven optimal control of a SEIR model for COVID-19,” arXiv:2012.00698, first submitted 1 December 2020; published in *Communications on Pure and Applied Analysis*, DOI: 10.3934/cpaa.2021093.
2. D. Ding, Q. Ma, and X. Ding, “An unconditionally positive and global stability preserving NSFD scheme for an epidemic model with vaccination,” *International Journal of Applied Mathematics and Computer Science* 24 (2014), 635–646. This is supporting background on structure-preserving epidemic discretization, not coverage of the present equation (3.1) identity.
