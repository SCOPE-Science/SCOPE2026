# Independent mathematical audit

## correctness

PASS

The polynomial generator identities are correct. Writing \(s=|X|^2\), \(R=\operatorname{Re}(\overline XY)\), and \(I=\operatorname{Im}(\overline XY)\), stationarity of \(Ls=2a(R-s)\) gives \(\int R=S\), while stationarity of \(LI=(c_1-a)I+c_2(s+R)\) gives \((c_1-a)\int I+2c_2S=0\). The displayed observable \(G=aR-(a+c_1)s/2\) satisfies \(LG=|\dot X|^2-ac_2I+a(2c_1-a-Z)s\). Eliminating \(\int I\) gives the claimed exact weighted-height identity. The auxiliary coboundary \(L(s-2aZ)=-2as+2abZ\) gives the mean law. On \(c_1=a\), \(c_2\ne0\), the \(I\)-balance forces \(S=0\), invariance then forces \(X=Y=0\), and the remaining scalar contraction forces the origin atom. The symbolic package verifier checks every polynomial identity exactly.

## originality

PASS

The complete boundedness paper and the complete later bifurcation paper were read. The first contains the same system and the transient identity derived from \(V=|X|^2-2aZ\), but develops ultimate bounds rather than stationary invariant-measure balances. The second derives Hopf thresholds and explicit rotating periodic solutions; its orbit height is consistent with the audited balance, but it does not state the measure-wide derivative-energy identity or the exclusion of every nontrivial compact invariant probability on \(c_1=a,\ c_2\ne0\). Resultary searches found no stronger same-object theorem.

## value

PASS

The theorem converts known trajectory algebra into a new exact statistical constraint for every compact recurrent state and identifies a sharp parameter plane where all compact recurrence collapses to the origin. It also explains the height of a published rotating orbit as one instance of a measure-wide law. That is a motivated structural recurrence result, not a routine restatement of an ultimate-bound estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
