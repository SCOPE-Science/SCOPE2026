# Independent mathematical audit

## correctness

PASS

The parameterized certificate reconstructs the source proof family exactly. With \(s=r^2=7/120\), \(L=32/45\), and \(U=23/30=1-4s\), the generalized fallback weight is \(\eta=49/21600\), the universal covering estimate certifies an integer cover cardinality at most 4702, the binary truncation condition holds at \(N=107\), and \((3/4)^{27}<\eta(3-2/L)\) supplies the multi-outcome positivity margin. Thus the certified message alphabet is \(4702\,4809^{27}<2^{343}\). The lower certificate analysis is also valid within the explicitly stated proof family: the global bounds force \(N\ge97\), \(n\ge26\); maximizing the multi-outcome margin over \(L\) gives the displayed one-variable function \(T(s)\), whose monotonicity on the needed interval and four exact threshold checks force the stated cover-bound lower values for \(n=26,27,28,29\); each makes the certified alphabet exceed \(2^{342}\), and \(n\ge30\) is excluded by the universal \(K\ge2304\) certificate bound. Exact rational/integer replay agreed with every displayed inequality. The conclusion is therefore sharp only for certificates that use this parameterized architecture and only the source's universal cover estimate, exactly as claimed.

## originality

PASS

The exact primary preprint was materially inspected at the finite qutrit construction, multi-outcome extension, and its optimization remark. It gives the published 357-bit certificate and explicitly introduces variable covering radius and fallback interval with \(\eta=12r^4(U-L)\), then says that improving the communication bound requires balancing covering size against truncation length and does not pursue the optimization. No inspected source states the 343-bit feasible point or the matching 342-bit impossibility inside this proof family. Targeted Resultary search likewise returned no equivalent certificate.

## value

PASS

The result improves the best explicit exact qutrit communication certificate in the motivating construction by fourteen bits and, within the clearly bounded architecture and cover input, proves that the next bit cannot be reached. This is a natural quantitative optimization of a current exact protocol, not a claim about the unknown globally optimal classical simulation cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
