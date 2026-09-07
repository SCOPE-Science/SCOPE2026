#!/usr/bin/env bash
# Rerun all verification in minutes. Stdlib python3 only.
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "== versions =="
python3 --version
echo "== verify_rect (orientation predicates) =="
python3 "$DIR/verify_rect.py" "$DIR/coords_K57_rect.json" "$DIR/crossing_list.csv"
echo "== verify_rect_second (rational parametric) =="
python3 "$DIR/verify_rect_second.py"
echo "== verify_planarity (rotation + Kuratowski control) =="
python3 "$DIR/verify_planarity.py"
echo "== hashes =="
sha256sum "$DIR/coords_K57_rect.json" "$DIR/rotation_K57_36.json" "$DIR/crossing_list.csv" "$DIR/verify_rect.py" "$DIR/verify_rect_second.py" "$DIR/verify_planarity.py" 2>/dev/null || shasum -a 256 "$DIR/"*
echo "ALL RERUN CHECKS PASS"
