# Independent mathematical audit

## correctness

PASS

PASS: For synchronous Greenberg-Hastings 0/1/2 rule on K_{a,b,c}, a rainbow transversal triangle (all three colors across parts) rotates and cannot lose excitation. Conversely, with all three colors globally present but no transversal rainbow, Hall SDR theorem forces two parts to have union size one, hence both monochromatic in the same state j; unique remaining part contains both other states. A direct update table shows extinction at t=2,3,4 when j=2,1,0 respectively, including the possibility j is also in exceptional part. For globally at most two states, time-1 {0,2}, time-2 {1,2}, time-3 generally {0,1}, and time-4 {0,1} with all excited vertices confined to one mixed part. For a part of size k the number of exceptional assignments containing both other colors is q_k=3^k−2^{k+1}+1, giving Q=sum q. Therefore d0=1, d1=2^N−1, d2=2^N−1+Q, d3=2^N+4−S+Q, d4=S−6+Q, dt>=5=0; sum E=3*2^N−3+3Q. Sharp cutoff 3 only at (1,1,1), otherwise 4. Independent direct vertex-state simulation verified all 10 triples with 1<=a<=b<=c<=3 (32670 labelled configurations).

## originality

PASS

PASS, best of knowledge with a specific antecedent: Gravner/Lyu/Sivakoff and Doba establish graph-circulation/cycle criteria and qualitative sustained excitation or extinction. A previously published complete-multipartite three-cycle census (source identifier 2327e9a1-48f2-4b71-8d77-fd24dccd688a) already establishes four-step entry to periodic behavior and counts periodic initial configurations; these are credited. A count of periodic states is not the labelled attraction-basin first-hitting-time histogram, and the inspected prior sources do not furnish the present five coefficients or the rainbow-SDR criterion as a complete basin count. Unexamined full earlier SCOPE source remains priority risk.

## value

PASS

PASS: The full labelled extinction-basin time histogram, exact combinatorial rainbow-transversal criterion and sparse-vs-balanced tripartite extinction probability asymptotics provide a natural dynamical classification beyond the already known entry-to-periodicity bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
