Reproduce the complete finite classification from the C++17 source files:

  g++ -std=c++17 -O2 -Wall -Wextra enumerate.cpp -o enumerate
  g++ -std=c++17 -O2 -Wall -Wextra crosscheck.cpp -o crosscheck
  ./enumerate
  ./crosscheck

Each program prints one "length" record per tested cycle length, for all lengths one through the corresponding minimum, and one "orbit" record per canonical representative at the minimum. Both length-record streams agree with checks.csv; enumerate.cpp orbit records agree with orbits.csv. For crosscheck.cpp the last field of each orbit line is the representative (orbit sizes follow from full periods and are recorded in orbits.csv).

Each exhaustive enumeration is complete: every integer in the candidate range is checked, and the covering predicate compares against all binary target patterns. No random seeds, optional packages, or external network resources are needed.
