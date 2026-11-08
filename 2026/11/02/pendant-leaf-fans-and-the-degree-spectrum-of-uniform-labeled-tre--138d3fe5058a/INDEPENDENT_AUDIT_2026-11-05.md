# Independent mathematical audit

## correctness

PASS

A pendant k-fan consists of k specified degree-one labels attached to one center c. Deleting them bijects this event with one uniform Cayley tree on the remaining m=n−k vertices; n*C(n−1,k)=m*C(n,k) choices yield E[S]=C(n,k)m^(m−1)/n^(n−2). Conditional on that event, the forced k leaves contribute k to D_{n,1}, the center has its residual degree shifted by k, and the other m−1 vertices have the ordinary m-tree degree law p_m(j)=P(1+Bin(m−2,1/m)=j). Subtracting the unconditional n p_n(r) and summing indicators gives the stated exact covariance, with m=2 boundary p_2(1)=1. First-order fixed-j binomial expansion yields (m−1)p_m(r)−n p_n(r)→−(k+1)e^−1/(r−1)! and E[S]/n→e^−k/k!, giving the displayed limit. Its sign for r>=k+1 is sign[(r−1)!/(r−k−1)!−(k+1)], positive from r=k+1 for k>=3, while for k=2 it is negative at r=3 and positive from 4. These strict signs are pointwise in fixed k,r, not uniform when degree grows. Independent separate Prüfer decoding checked all n^(n−2) trees for n=4,5,6 and every allowed (k,r), obtaining exact rational mean/covariance equalities.

## originality

PASS

The paper on fixed fringe counts in random degree-constrained trees proves broad asymptotic joint fluctuation theorems and may encode related local covariances, but the inspected sections do not explicitly give the finite all-n covariance of unrestricted-center pendant k-fans with every degree bin or its complete sign rule. General Prüfer multinomial counts are old, not claimed as novel. The derived mixed statistic and sign boundary represent the specific assessed contribution, qualified by possible implicit earlier generating-function results.

## value

PASS

Pendant k-fans quantify repeat leaf attachments at one vertex and are relevant to local tree symmetry, while D_{n,r} is the natural global degree spectrum. Their exact finite-size cross covariance and strict positive–negative–positive degree rule (with the k=2 exception) give interpretable dependencies unavailable from marginal expectations alone; the full n,k,r classification is a motivated extension of random-tree local statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
