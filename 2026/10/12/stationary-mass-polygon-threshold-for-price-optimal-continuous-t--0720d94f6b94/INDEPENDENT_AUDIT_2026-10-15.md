# Independent mathematical audit

## correctness

PASS

The variational spectral quotient is min_z (∑w_i z_i²)/(z^T[diag(p)-pp^T]z), with V positive definite by pi_0>0. Substitution x_i=w_i/gap gives the primal SDP min∑c_i x_i s.t. diag(x)-V PSD; strict primal feasibility and Gram dual diag(Y)=c yield dual S-min||∑pi_i u_i||². The sharp polygon resultant lower bound is delta, attained by planar closing or collinear opposite vectors. For delta=0, x=p, slack ppT rank1, complementary slackness with nonzero Gram vectors forces uniqueness. For delta>0, explicit x_j=pi_j(1-delta/sqrt(c_j)) and x_i=pi_i(1+delta/sqrt(c_i)) produce a PSD slack by positive leaf-away-from-j Schur block with zero complement, rank m-1; rank-one dual kernel forces uniqueness. Budget-normalize by T and get required multiplicities. All positivity and transition boundary cases were checked.

## originality

PASS

PASS best-of-knowledge: Göring–Helmberg–Wappler (2005) give related graph spectral/embedding SDP and unweighted variance framework, and Boyd–Diaconis–Xiao and Jafarizadeh address discrete-time mixing; their stated objectives/feasibility constraints do not establish the simultaneous arbitrary stationary-mass and independent-price continuous-time star closed formula. Source full/primary sections read for 2005. Resultary returned other spectral-mixing findings with different graphs/objectives. Historical weighted-tree SDP reductions may hide a logically equivalent theorem, retained as risk; search failure alone is not a novelty proof.

## value

PASS

A complete and sharp optimization classification on the canonical star graph under two physically meaningful heterogeneities (vertex occupancy masses and per-edge conductance costs) determines all optimal rates, sharp phase boundary, uniqueness and eigengap multiplicity; mass imbalance causes a transition even with equal prices. Not merely a fixed example, parameter renaming or known unweighted-star evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
