# Independent mathematical audit

## correctness

PASS

For any agent \(i\) and her top-\(k\) set \(T_i(k)\), appearing among the first \(k\) priority positions guarantees that at least one object in \(T_i(k)\) remains, so RSD gives \(p_i(T_i(k))\ge k/n\). With exactly two preference types \(A,B\), equal treatment of equals gives common lotteries \(x^A,x^B\) for the two types. If there are \(r\) agents of type \(A\) and \(s=n-r\) of type \(B\), feasibility over a type-\(A\) top-\(k\) set \(T\) gives \(r x^A(T)+s x^B(T)=k\). Hence \(s(x^A(T)-x^B(T))=n x^A(T)-k\ge0\). Thus type \(A\) does not stochastically envy type \(B\); the symmetric argument handles type \(B\), and same-type agents have identical lotteries. The printed three-agent witness indeed violates stochastic-dominance envy-freeness, and the exact package census finds 72 failures among 216 strict labeled profiles, all using three distinct orders, in two symmetry classes of size 36.

## originality

PASS

Bogomolnaia and Moulin establish the general stochastic-dominance fairness benchmark and show that Random Priority need not be envy-free. Hosseini, Larson and Cohen give the same three-agent failing preference pattern used here, so that witness is treated as prior. Their complete accessible text does not state the all-\(n\) two-preference-type domain theorem. Targeted searches for two rankings or two preference types under RSD found no equivalent theorem; a recent axiomatic characterization of RSD addresses market-size consistency rather than this preference-domain restriction.

## value

PASS

Random Priority is a canonical allocation mechanism whose stochastic-dominance envy failure is a standard limitation. The theorem identifies a simple, maximal-at-the-smallest-failure structural preference-diversity regime where full stochastic-dominance envy-freeness is restored, and the three-agent census shows that three distinct types are already sufficient for failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
