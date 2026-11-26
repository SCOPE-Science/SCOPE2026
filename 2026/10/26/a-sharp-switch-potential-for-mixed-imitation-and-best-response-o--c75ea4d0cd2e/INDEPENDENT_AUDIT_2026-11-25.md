# Independent mathematical audit

## correctness

PASS

Subtracting counterfactual neighbor earnings gives the A-best-response advantages (a+b)(k−1−t) for a current A and (a+b)(k−t) for a current B. Subtracting actual earnings gives (a+b)(k−w), with w=t+(R−S)/(a+b) strictly between t and t+1 because R−S and P−T are positive and sum to a+b. Below h=floor(t)+1 only decreases occur, above h only increases; below h at least two B agents are present, so a B imitator is not forced to copy a disfavored A, and the symmetric singleton check holds above h. At h either direction improves |k−h|. Since 1≤h≤n−1, there are at most n−1 switches, and persistence precludes being stuck at a nonabsorbing profile. Only k=h can be mixed absorbing. There B best responders strictly prefer A; A best responders strictly prefer B unless t=h−1, when w<h and every B flips on activation. Off an earnings tie the disfavored side contains a switcher; at an earnings tie t<h<t+1 and any best responder switches. With pure imitation at a tie a singleton lacks a like-strategy neighbor, while any split with at least two of each strategy persists. The four-player example and the n−1-switch construction check directly, including n=2; the latter extends to a persistent schedule. Independent direct-payoff enumeration (`python3 /workspace/independent_checks.py 2`) checked 21,824 type/profile/payoff cases and 123,776 activations. The analytical threshold and tie arguments provide the arbitrary-n proof.

## originality

PASS

The closest hybrid update paper covers sparse trees and qualitative equilibration. The supported distinct claim here is the strict common per-switch potential for homogeneous complete networks with the stated neighbor-only rules, its sharp uniform switch count, and its resulting exact mixed-type absorption classification; prior general pure-imitator equilibration is not claimed original.

## value

PASS

This resolves a natural dense-network case with one common strict potential across behavioral mixtures and every asynchronous activation, a sharp worst-case switch budget, and a precise consensus/coexistence distinction. A bound on actual switches is useful even when fair activation imposes no elapsed-time bound. Homogeneous payoffs, complete graphs, fixed types and the stated tie rules are essential limits of the assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
