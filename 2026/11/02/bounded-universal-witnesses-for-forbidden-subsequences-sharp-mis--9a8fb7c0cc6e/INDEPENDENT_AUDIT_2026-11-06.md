# Independent mathematical audit

## correctness

PASS

The host H_K(v)=pi_1^K v_1 pi_2^K...v_(m-1)pi_m^K (pi_i permutes alphabet without v_i) avoids v under greedy matching and contains each length<=K v-avoiding word by decomposing it at greedy matches into alphabet-restricted blocks. The insertion sphere of length-(k-1) pattern has (q-1)k+1 distinct k-word elements, proved by moving identical letters through runs and Parikh-vector uniqueness; each absent shorter subsequence forces those longer absences and H_k(v) attains the bound. For unary v=a^m and K>=m, an avoiding universal host contains exactly m-1 a letters; every gap must contain each length t=K-m+1 non-a constant word, giving the sharp lower m(q-1)t+m-1, attained by permutation^t blocks. Independent literal subsequence checks covered 2626 cases and brute-force unary shortest lengths, while packaged verify.py enumerates additional finite samples. K=0/m=1 boundaries were examined. Infinite assertions rest on constructions and lower bounds.

## originality

PASS

Classical Higman–Haines ideals establish qualitative subsequence-avoidance structure, while Fleischmann et al. (2022) study m-nearly-k-universal words and sharp missing-one-word cases. The assessed contribution is an explicit universal bounded host for every principal avoidance class plus the exact all-alphabet insertion-sphere defect jump and unary optimal length. The Resultary full-support insertion-radius finding measures a different operation (letters inserted to reach full universality). Prior structural theory may imply host existence but the sharp quantitative unary cost and entire spectrum were not observed in inspected statements.

## value

PASS

Exact natural language-theoretic universal hosts for principal forbidden-subsequence ideals, sharp missing spectrum when (k-1)-universality fails, and an optimal length for unary forbidden patterns give reusable extremal bounds for subsequence universality and compact witness constructions. Not an arbitrary isolated enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
