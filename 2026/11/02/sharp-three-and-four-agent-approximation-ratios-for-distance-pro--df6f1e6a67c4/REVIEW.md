# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/2/RESULT.md. The frozen three-agent proof had the wrong attaining comparator (both endpoints of the shortest edge can incur v, not u; e.g. 0,1,4). The repair pairs one endpoint with the third report. The triangle-inequality lower bound then gives OPT_2=u, and the ratio formula follows from N=u(2v+w) and v<=w. For four agents, the repair uses a fixed nonempty assignment with total assigned distance K no greater than the ORIGINAL comparison cost, even after relocating an unused center. In the 1+3 split, the cross contribution is at most PD−sum D_i e_i and the inside contribution at most P²+sum d_ij min(D_i,D_j). Sorting the D_i makes the cancellation inequality follow from (v−w)(D_q−D_p)+u(D_r−D_p)>=(u+v−w)(D_q−D_p)>=0. Hence N<=PZ<=2KZ. In the 2+2 split cross-pair costs are at most u+v and either within-pair sample costs at most H, the cross-distance sum; thus N<=2(u+v)H<=2KZ. Taking the infimum covers nonattainment and OPT_2=0; Z=0 is handled separately. Independent enumeration of pair costs on (0,T,T+1,T+2) gives cross costs (3,2,3) and inside costs (T+1,T+1,T+2) in increasing pair order, so N=12T+13 and Z=3T+7, with OPT_2=2 by the clustered median and the shared-center lower bound. The sharp distinct-report line families give the two suprema.

## originality

PASS

The repaired result credits the established rule and the indexed line-case overlap. The distinct surviving result is the exact unrestricted metric-space comparison at three and four agents, including sharpness at four distinct line reports. The strongest inspected indexed hits constrain the domain to line first surplus or exactly three occupied line sites.

## value

PASS

Three and four agents are the first nontrivial population and the first allowing both nonempty 1+3 and 2+2 comparison partitions. Resolving the first two tight guarantees for a known rule against potentially off-report optimum locations materially improves the general factor four on these populations; the cancellation bound for the triple cluster explains why the stronger guarantee is metric rather than line-specific.

The dated certificate retains the supplied scientific assessment, sources and limitations.
