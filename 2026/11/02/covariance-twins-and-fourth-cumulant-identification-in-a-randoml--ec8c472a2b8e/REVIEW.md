# Scientific review

## Correctness — PASS

The zero-mean stationary switched diffusion has a well-defined causal stochastic-integral construction and moments of every fixed even order. Its joint-state second-moment equations give \(C(0)=D(2/k+1/q)\) and \(C'(0+)=-D\). The conditional propagator is a two-by-two matrix with characteristic polynomial \(z^2+(k+2q)z+kq\), proving exact covariance invariance under \((q,k,D)\mapsto(k/2,2q,D)\). Third and fourth right derivatives recover \(P=kq\) and \(L=k+2q\), so the unordered pair \(\{k,2q\}\) and **exactly** its two possible assignments are determined. Fourth-moment generator identities give \(\kappa_4=D^2(9/q^2+6/(qk))\), strictly separating twins off the fixed line. This derivation supplies the infinite-parameter-range proof; the independent matrix-exponential and symbolic program checks are corroboration, not proof of completeness.

## Originality — PASS (qualified)

The originating physical model, stationary second moment and relaxation of one-time variance are established in Santra--Das--Nath (2021). The stationary fourth-moment identity is already present in the moment recurrence of Frydel (2024) and is explicitly **not** claimed as a new stand-alone result. The broad Markov-modulated OU framework of Huang and colleagues (2014) contains a matrix-exponential formula for forward covariance and could produce the specialized covariance upon calculation. The assessed new statement is not the forward formula: it is the exact two-to-one *inverse map*, its complete positive-parameter fiber classification, the nontrivial stiffness/switching involution, and the consequent non-Gaussian disambiguation. Searches did not locate this inverse theorem in the inspected sources or indexed related findings. The strongest novelty risk is that a broader system-identification theorem or an unrecognized statement in the general Markov-modulated theory may already imply the same inverse classification; independent priority review is not performed.

## Mathematical value — PASS

The inverse ambiguity answers a natural experimental calibration question for switching optical traps: even an ideal all-frequency position power spectrum cannot distinguish two physically different trap kinetics. The theorem both proves that the ambiguity has exactly two members (rather than just exhibiting an accidental equality) and gives a single higher-order observable that removes it, with an explicit reconstruction formula. This is a structural identifiability limit, not merely a small numerical improvement or a restatement of a previously tabulated fourth moment. It makes no finite-data statistical claim, and the extra use of a known moment identity does not itself establish originality.

## Closest literature and limitations

The strongest relevant forward-coverage comparator is the general covariance machinery of *Markov-modulated Ornstein-Uhlenbeck processes* (arXiv:1412.7952), §3.3. The model-specific sources are *Brownian motion under intermittent harmonic potentials* (arXiv:2104.00609), especially §§2–3, and *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap* (arXiv:2407.12213), especially §II, the moment recurrence and Appendix B. The semi-Markovian extension arXiv:2607.05173 discusses spatial moments but was not found to give this inverse covariance theorem. Novelty against all possible published inference work remains a residual risk. The proof applies only to symmetric on/off Markov switching, an exactly zero off stiffness and ideal stationary covariance; it does not compare complete joint two-time probability laws.

Self-review: passed. Independent audit: not yet performed.
