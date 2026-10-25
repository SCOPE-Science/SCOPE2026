# Independent mathematical audit

## correctness

PASS

The parity-of-adjacent-11-bits definition gives s_(2t)=(-1)^t and s_(2t+1)=(-1)^t s_t. Pairing a length-2^k window yields S_k(j)=U_(k-1)(floor(j/2)), with U_l(j)=-U_(l-1)(floor(j/2)) for l>=2. Exact slide invariance follows matching signed endpoint terms for odd shifts. Thus S_k(j)=(-1)^(k-2+q)(s_q-s_(q+1)), q=floor(j/2^(k-1)), for all j>=0,k>=3. Pairwise U1(2h),U1(2h+1) make exactly half of q zero; their nonzero signs balance over complete dyadic q blocks, giving proportions 1/4,1/2,1/4. Independently summed direct words for k=3..7 with arbitrary starts j<400 and verified histograms m=2..6. Infinite quantifiers rest on transfer proof.

## originality

PASS

The closely related full primary Marcovici–Stoll–Tahay paper studies averaged prefix correlations for generalized Rudin–Shapiro sequences. Its Theorems 2.10 and 2.12 give O(log N/N) frequency discrepancy and limiting pair frequency, neither a uniform exact moving dyadic S_k(j) value for every starting index nor half-window phase law. Earlier automatic-sequence complexity and finite Golay correlation articles concern different invariants. Best-of-knowledge originality PASS with explicit older block-recurrence risk.

## value

PASS

Sharp uniform three-valued discrepancy for every sliding dyadic window, exact phase by start interval, frequency law and adjacent-boundary-transition interpretation are structural exact facts about a canonical automatic sequence, significantly stronger than mean asymptotic cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
