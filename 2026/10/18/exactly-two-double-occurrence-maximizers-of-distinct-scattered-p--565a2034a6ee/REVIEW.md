# Independent mathematical audit

## correctness

PASS

For a fixed nonempty support every noncentral letter must use its two host positions in mirrored pairs, and those intervals strictly nest. If all intervals nest there is one even value and one odd value (only the innermost letter can be central). Otherwise there is no even value; a prescribed center fixes the palindrome value and three distinct feasible centers would force every interval pair to nest by choosing a center outside that pair. Thus equality in the total bound forces two values for every support separately. A disjoint pair of intervals prevents either letter enclosing the other, giving zero for that support. Pairwise intersection with distinct endpoints then puts every first occurrence before every second occurrence. On full support an even value forces the whole word to be the reversed-tail palindrome. Otherwise the two odd centers c,d require reversal of each pair other than {c,d}, which must be nonreversed and consecutive in first-appearance order. Any letter first appearing after both would have both of their intervals enclosing its interval, making either center impossible. So only the two highest letters can be swapped. If a support contains both swapped letters, there is one interior occurrence of each inside the other interval (the later opener and earlier closer, respectively), giving exactly the two odd values; all other supports have the even/odd nested pair. Counting the supports of size k containing the swapped pair yields the stated binomial correction and all lengths. The two canonical words are distinct at q=2 as well, and labeling gives q! choices for each. The q=1 host has only its singleton and doubleton values. The uploaded checker's finite matching/permutation tests were inspected, not executed; the interval argument proves the unbounded statement.

## originality

PASS

Credit Mahalingam–Pandoh not only for the sharp maximum and the nested witness, but also for the nested length spectrum, which is explicitly stated after Proposition 5.1. The distinct supported claim is the exhaustive equality classification, including the unique crossed canonical case, its length spectrum, and the resulting labeled multiplicities. No inspected comparator provides those results directly or by specialization.

## value

PASS

The balanced boundary of a prior extremal problem has a natural exact equality question. An exhaustive all-q result showing one nested and one genuinely nonpalindromic form answers it, and the crossed spectrum describes exactly how even values are traded for odd values at fixed support size. This is a structural classification beyond the known maximum and nested spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
