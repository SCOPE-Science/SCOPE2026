# Independent mathematical audit

## correctness

PASS

Original theoretical COCOB, not COCOB-Backprop, known bound L>0: G_t=G_(t-1)+|g_t|, theta_t=theta_(t-1)+g_t, Reward_t=Reward_(t-1)+(w_t-w_1)g_t, beta_t=L^-1 tanh(theta_t/(G_t+L)), w_(t+1)=w_1+beta_t(L+Reward_t). Balanced external negative-gradient input g_odd=L,g_even=-L yields theta_odd=L,theta_even=0, G_(2n-1)+L=(2n+1)L. Thus beta_(2n-1)=a_n/L, beta_even=0, a_n=tanh(1/(2n+1)); all w_(2n+1)=w1 and odd-round wealth unchanged. Even reward step consumes a_n fraction: W_n=W_(n-1)(1-a_n), P_n=prod(1-a_k), and w_(2n)-w1=a_n P_(n-1)=P_(n-1)-P_n. Averaging first T iterates gives exactly (1-P_floor(T/2))/T. Product identity 1-tanh x=e^-x/cosh x and harmonic sum H_(2n+1)-1-H_n/2 = (1/2)log n+log2+gamma/2-1+o establish P_n~C/sqrt n with convergent product C=e^(1-gamma/2)/(2prod cosh(1/(2k+1))); excursion ~C/(2n^1.5). The constant is independent of L. Independently replayed first five pairs for L=3 and nonzero starting iterate w1=1.2, all reset/wealth identities agree numerically. This is an externally prescribed sequence, not asserted realizable by one fixed objective.

## originality

PASS

Best-of-knowledge surviving original contribution; compare mathematical implication rather than titles/parameters. The original COCOB paper Algorithm 1 and theory establish update and scale-free bounds, emphasizing same-sign growth; no exact balanced period-two reset, telescoping average and n^-3/2 envelope was found in inspected algorithm/source discussion. Chen–Langford–Orabona later derive ODE-based parameter-free method, not the same discrete COCOB update. Resultary focused semantic search returned no matching COCOB periodic-outcome theorem, but absence is not priority proof.

## value

PASS

Period-two zero-drift input is a canonical stress test for a coin-betting optimizer and contrasts with the method paper’s same-sign growth example. The full exact reset, wealth and averaged-iterate laws quantify algorithm behavior and normalization independent of gradient scale; meaningful exact optimizer diagnostic beyond a vacuous zero-gradient check, despite narrow signal family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
